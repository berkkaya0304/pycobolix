import React from 'react';
import { QualityLabel } from '@/lib/data/types';
import styles from './QualityBadge.module.css';
import clsx from 'clsx';

interface QualityBadgeProps {
  label: QualityLabel;
}

export default function QualityBadge({ label }: QualityBadgeProps) {
  return (
    <span
      className={clsx(styles.badge, {
        [styles.high]: label === 'High',
        [styles.medium]: label === 'Medium',
        [styles.low]: label === 'Low',
      })}
    >
      {label} Maintainability
    </span>
  );
}
