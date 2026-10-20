import { createNavigation } from 'next-intl/navigation';
import { routing } from './routing';

// 基于 routing 生成类型安全的导航 API，供服务端/客户端组件使用
export const { Link, redirect, usePathname, useRouter, getPathname } =
  createNavigation(routing);
