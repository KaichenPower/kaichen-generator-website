'use client';
import { useCallback, useEffect, useRef, useState } from 'react';
import { useTranslations } from 'next-intl';
import { Link } from '@i18n/navigation';

type SlideText = { title: string; subtitle: string };

const slides = [
  { src: '/images/slides/slide-1.jpg', alt: 'Kaichen Power diesel generator factory' },
  { src: '/images/slides/slide-2.jpg', alt: 'Kaichen Power genset production workshop' },
  { src: '/images/slides/slide-3.jpg', alt: 'Kaichen Power container and silent generator sets' },
  { src: '/images/slides/slide-4.jpg', alt: 'Kaichen Power open diesel generators' },
  { src: '/images/slides/slide-5.jpg', alt: 'Kaichen Power mobile trailer generators' },
];

export default function Slideshow() {
  const t = useTranslations('home');
  const slideTexts = (t.raw('slides') as SlideText[]) || [];
  const [index, setIndex] = useState(0);
  const timer = useRef<ReturnType<typeof setInterval> | null>(null);

  const go = useCallback((next: number) => {
    setIndex(((next % slides.length) + slides.length) % slides.length);
  }, []);

  useEffect(() => {
    timer.current = setInterval(() => go(index + 1), 4500);
    return () => {
      if (timer.current) clearInterval(timer.current);
    };
  }, [index, go]);

  const current = slideTexts[index] ?? { title: '', subtitle: '' };

  return (
    <div className="slideshow">
      <div
        className="slideshow-track"
        style={{ transform: `translateX(-${index * 100}%)` }}
      >
        {slides.map((s, i) => (
          <div key={s.src} className="slideshow-slide" aria-hidden={i !== index}>
            <img src={s.src} alt={s.alt} width={1920} height={979} loading={i === 0 ? 'eager' : 'lazy'} />
          </div>
        ))}
      </div>

      {/* 暗化遮罩 + 文案叠加（每张图文字不同，左对齐） */}
      <div className="slideshow-overlay" />
      <div className="slideshow-caption container">
        <div className="caption-inner">
          <span className="hero-badge">{t('heroBadge')}</span>
          <h1>{current.title}</h1>
          <p>{current.subtitle}</p>
          <div className="hero-actions">
            <Link href="/products" className="btn btn-accent">
              {t('cta')}
            </Link>
            <Link href="/contact" className="btn btn-outline">
              {t('secondaryCta')}
            </Link>
          </div>
        </div>
      </div>

      <button
        type="button"
        className="slideshow-arrow slideshow-prev"
        aria-label="Previous slide"
        onClick={() => go(index - 1)}
      >
        ‹
      </button>
      <button
        type="button"
        className="slideshow-arrow slideshow-next"
        aria-label="Next slide"
        onClick={() => go(index + 1)}
      >
        ›
      </button>

      <div className="slideshow-dots">
        {slides.map((s, i) => (
          <button
            key={s.src}
            type="button"
            className={`slideshow-dot${i === index ? ' is-active' : ''}`}
            aria-label={`Go to slide ${i + 1}`}
            aria-current={i === index}
            onClick={() => go(i)}
          />
        ))}
      </div>
    </div>
  );
}
