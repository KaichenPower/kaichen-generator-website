'use client';
import { useState } from 'react';
import { useTranslations } from 'next-intl';

// Web3Forms 配置
const ACCESS_KEY = '9e488395-317d-4363-9f97-53259ba15d11';
const ENDPOINT = 'https://api.web3forms.com/submit';

type Props = {
  subject?: string;
  productName?: string;
  productUrl?: string;
};

type Status = 'idle' | 'sending' | 'ok' | 'error';
type FieldKey = 'name' | 'email' | 'phone' | 'country' | 'product' | 'message';

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export default function EnquiryForm({ subject, productName = '', productUrl = '' }: Props) {
  const pp = useTranslations('productsPage');
  const cp = useTranslations('contactPage');
  // 记录表单挂载时间，用于拦截"秒提交"的机器人
  const [mountedAt] = useState(() => Date.now());
  const [cooldown, setCooldown] = useState(false);
  const [form, setForm] = useState({
    name: '',
    email: '',
    phone: '',
    country: '',
    // 产品页：把"产品名称：xxx + 产品链接：yyy"合成一个字段，可编辑
    product: subject
      ? `${cp('productNamePrefix')} ${productName}\n${cp('productLinkPrefix')} ${productUrl}`
      : '',
    productUrl, // 规范产品网址（提交用，界面不单独显示）
    message: '',
    botcheck: '', // 蜜罐字段，留空
  });
  const [errors, setErrors] = useState<Partial<Record<FieldKey, string>>>({});
  const [status, setStatus] = useState<Status>('idle');

  // 单字段校验：必填 + 邮箱格式
  function validateField(key: FieldKey, value: string): string | undefined {
    const v = value.trim();
    if (!v) return cp('reqError');
    if (key === 'email' && !EMAIL_RE.test(v)) return cp('emailInvalid');
    return undefined;
  }

  // 校验全部必填字段
  function validateAll(): boolean {
    const next: Partial<Record<FieldKey, string>> = {};
    (['name', 'email', 'phone', 'country', 'message'] as FieldKey[]).forEach((k) => {
      const err = validateField(k, form[k]);
      if (err) next[k] = err;
    });
    const prodErr = validateField('product', form.product);
    if (prodErr) next.product = prodErr;
    setErrors(next);
    return Object.keys(next).length === 0;
  }

  // 更新字段：实时清除已修复的错误
  function update(k: keyof typeof form) {
    return (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
      const val = e.target.value;
      setForm((prev) => ({ ...prev, [k]: val }));
      if (k === 'botcheck') return;
      const fk = k as FieldKey;
      setErrors((prev) => {
        const err = validateField(fk, val);
        const next = { ...prev };
        if (err) next[fk] = err;
        else delete next[fk];
        return next;
      });
    };
  }

  // 失焦时校验并提示
  function onBlur(key: FieldKey) {
    return () => {
      const err = validateField(key, form[key]);
      setErrors((prev) => (err ? { ...prev, [key]: err } : { ...prev, [key]: undefined }));
    };
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    // 蜜罐被填了 → 机器人，直接丢弃
    if (form.botcheck) return;
    // 表单挂载不足 3 秒就提交 → 极可能是脚本机器人，静默丢弃
    if (Date.now() - mountedAt < 3000) return;
    // 冷却期内禁止重复提交
    if (cooldown) return;

    // 提交前整体校验，有错则阻止并提示
    if (!validateAll()) return;

    setStatus('sending');

    const payload = {
      access_key: ACCESS_KEY,
      subject: `${subject || cp('formTitle')}${form.product ? ' — ' + form.product : ''}`,
      from_name: form.name,
      name: form.name,
      email: form.email,
      phone: form.phone,
      country: form.country,
      product: form.product || subject || '',
      product_url: form.productUrl,
      message: form.message,
    };

    try {
      const res = await fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
      const data = await res.json();
      setStatus(data && data.success ? 'ok' : 'error');
    } catch {
      setStatus('error');
    }
    // 无论成败，进入 20 秒冷却，防频繁刷
    setCooldown(true);
    window.setTimeout(() => setCooldown(false), 20000);
  }

  const placeholders: Record<FieldKey, string> = {
    name: cp('phName'),
    email: cp('phEmail'),
    phone: cp('phPhone'),
    country: cp('phCountry'),
    product: cp('phProduct'),
    message: cp('phMessage'),
  };

  const field = (key: FieldKey, value: string, onChange: any, onBlurFn: any) => {
    const err = errors[key];
    return (
      <div className={`form-field${err ? ' has-error' : ''}`}>
        {err && <span className="field-error">{err}</span>}
        <input
          placeholder={placeholders[key]}
          value={value}
          onChange={onChange}
          onBlur={onBlurFn}
          aria-invalid={err ? true : undefined}
        />
      </div>
    );
  };

  return (
    <div className="form-card">
      {status === 'ok' && <div className="form-success">{cp('success')}</div>}
      {status === 'error' && <div className="form-error">{cp('formError')}</div>}
      <h3 style={{ marginTop: 0 }}>{subject ? cp('quoteHeading') : pp('enquiryTitle')}</h3>
      <form onSubmit={handleSubmit} noValidate>
        {/* 蜜罐：对用户隐藏，机器人填了会被丢弃 */}
        <input
          type="text"
          name="botcheck"
          value={form.botcheck}
          onChange={update('botcheck')}
          style={{ position: 'absolute', left: '-9999px', opacity: 0 }}
          tabIndex={-1}
          autoComplete="off"
          aria-hidden="true"
        />
        <div className="form-grid">
          <div className="form-field">
            <label>
              {cp('name')} <span style={{ color: 'red' }}>*</span>
            </label>
            {field('name', form.name, update('name'), onBlur('name'))}
          </div>
          <div className="form-field">
            <label>
              {cp('emailInput')} <span style={{ color: 'red' }}>*</span>
            </label>
            {field('email', form.email, update('email'), onBlur('email'))}
          </div>
          <div className="form-field">
            <label>
              {cp('phone')} <span style={{ color: 'red' }}>*</span>
            </label>
            {field('phone', form.phone, update('phone'), onBlur('phone'))}
          </div>
          <div className="form-field">
            <label>
              {cp('country')} <span style={{ color: 'red' }}>*</span>
            </label>
            {field('country', form.country, update('country'), onBlur('country'))}
          </div>
        </div>
        <div className="form-field">
          <label>
            {cp('product')} <span style={{ color: 'red' }}>*</span>
          </label>
          {subject ? (
            <>
              <textarea
                rows={3}
                value={form.product}
                onChange={update('product')}
                onBlur={onBlur('product')}
                aria-invalid={errors.product ? true : undefined}
              />
              {errors.product && <span className="field-error">{errors.product}</span>}
            </>
          ) : (
            <>
              <input
                placeholder={cp('phProduct')}
                value={form.product}
                onChange={update('product')}
                onBlur={onBlur('product')}
                aria-invalid={errors.product ? true : undefined}
              />
              {errors.product && <span className="field-error">{errors.product}</span>}
            </>
          )}
        </div>
        <div className="form-field">
          <label>
            {cp('message')} <span style={{ color: 'red' }}>*</span>
          </label>
          <textarea
            rows={5}
            placeholder={cp('phMessage')}
            value={form.message}
            onChange={update('message')}
            onBlur={onBlur('message')}
            aria-invalid={errors.message ? true : undefined}
            className={errors.message ? 'input-error' : ''}
          />
          {errors.message && <span className="field-error">{errors.message}</span>}
        </div>
        <button
          type="submit"
          className="btn btn-accent"
          disabled={status === 'sending' || cooldown}
        >
          {status === 'sending' && <span className="btn-spinner" aria-hidden="true" />}
          {status === 'sending'
            ? cp('sending')
            : subject
              ? cp('submit')
              : pp('enquirySend')}
        </button>
        {cooldown && <p className="form-error" style={{ marginTop: '0.6rem' }}>{cp('tooFrequent')}</p>}
        <p className="form-note">{pp('enquiryNote')}</p>
      </form>
    </div>
  );
}
