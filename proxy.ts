import createMiddleware from 'next-intl/middleware';
import { routing } from './i18n/routing';

// Next.js 16 已将 Middleware 更名为 Proxy。
// 使用统一的 routing 配置创建代理，负责语言前缀路由与根路径跳转。
export default createMiddleware(routing);

export const config = {
  // 匹配所有路径，但跳过内部资源
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
};
