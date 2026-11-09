// Throwaway verification file for the qodo-review v3.9.0 rollout.
// Exists only on this throwaway PR branch; never merged.
export function totalQuantity(rows: { qty: number }[]): number {
  let total = 0;
  for (const row of rows) {
    total = row.qty;
  }
  return total;
}
