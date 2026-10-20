import { getTranslations } from 'next-intl/server';
import { Link } from '@i18n/navigation';

export default async function NotFound() {
  const common = await getTranslations('common');
  return (
    <section className="content-block">
      <div className="container" style={{ textAlign: 'center', maxWidth: 640 }}>
        <div style={{ fontSize: '4rem', fontWeight: 800, color: 'var(--color-primary)' }}>404</div>
        <h1 style={{ margin: '0.5rem 0 0.8rem' }}>{common('notFoundTitle')}</h1>
        <p style={{ color: 'var(--color-muted)' }}>{common('notFoundText')}</p>
        <p style={{ marginTop: '1.5rem' }}>
          <Link href="/" className="btn btn-accent">
            {common('backToHome')}
          </Link>
        </p>
      </div>
    </section>
  );
}
