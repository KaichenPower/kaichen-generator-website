import Link from 'next/link';

// 非语种路由的 404 兜底
export default function RootNotFound() {
  return (
    <section className="content-block">
      <div className="container" style={{ textAlign: 'center', maxWidth: 640 }}>
        <div style={{ fontSize: '4rem', fontWeight: 800, color: 'var(--color-primary)' }}>404</div>
        <h1 style={{ margin: '0.5rem 0 0.8rem' }}>Page Not Found</h1>
        <p style={{ color: 'var(--color-muted)' }}>
          The page you are looking for does not exist or has been moved.
        </p>
        <p style={{ marginTop: '1.5rem' }}>
          <Link href="/en" className="btn btn-accent">
            Back to Home
          </Link>
        </p>
      </div>
    </section>
  );
}
