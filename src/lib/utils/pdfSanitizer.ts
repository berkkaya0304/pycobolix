/**
 * PDF Sanitizer Utility
 * Prevents "unsupported number" crashes in @react-pdf/renderer by normalizing anomalous data.
 */

const MAX_SAFE = 1000000;

export const safeNumber = (val: any, fallback = 0): number => {
  if (typeof val !== 'number' || isNaN(val) || !isFinite(val)) return fallback;
  if (val > MAX_SAFE) return MAX_SAFE;
  if (val < -MAX_SAFE) return -MAX_SAFE;
  return val;
};

export const deepSanitize = (obj: any, path = 'root'): any => {
  if (typeof obj === 'number') {
    const sn = safeNumber(obj);
    if (sn !== obj) {
      console.error(`[PDF Debug] Sanitized anomaly at ${path}: ${obj} -> ${sn}`);
    }
    return sn;
  }
  if (Array.isArray(obj)) {
    return obj.map((v, i) => deepSanitize(v, `${path}[${i}]`));
  }
  if (obj && typeof obj === 'object') {
    return Object.fromEntries(
      Object.entries(obj).map(([k, v]) => [k, deepSanitize(v, `${path}.${k}`)])
    );
  }
  return obj;
};
