import type { Metadata } from 'next';
import './globals.css';
import Navbar from '@/components/Nav/Navbar';
import Tutorial from '@/components/Tutorial/Tutorial';
import { ThemeProvider } from '@/components/ThemeProvider';
import { LanguageProvider } from '@/lib/i18n/LanguageContext';
import { Toaster } from 'sonner';

export const metadata: Metadata = {
  title: 'Pycobolix | Modernizing Heritage',
  description: 'Visualize COBOL to Python modernization metrics',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider
            attribute="class"
            defaultTheme="system"
            enableSystem
            disableTransitionOnChange
        >
          <LanguageProvider>
            <Navbar />
            <div className="page-wrapper">{children}</div>
            <Tutorial />
            <Toaster richColors position="top-right" duration={2500} />
          </LanguageProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}
