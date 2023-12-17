// uncrustify:off
#include <math.h>
// uncrustify:on
#include <stdint.h>
#include <string.h>

#include "nvim/math.h"

#ifdef INCLUDE_GENERATED_DECLARATIONS
# include "math.c.generated.h"
#endif

int xfpclassify(double d)
  FUNC_ATTR_CONST
{
  uint64_t m;

  memcpy(&m, &d, sizeof(m));
  int e = 0x7ff & (m >> 52);
  m = 0xfffffffffffffULL & m;

  switch (e) {
  default:
    return FP_NORMAL;
  case 0x000:
    return m ? FP_SUBNORMAL : FP_ZERO;
  case 0x7ff:
    return m ? FP_NAN : FP_INFINITE;
  }
}

int xisinf(double d)
  FUNC_ATTR_CONST
{
  return FP_INFINITE == xfpclassify(d);
}

int xisnan(double d)
  FUNC_ATTR_CONST
{
  return FP_NAN == xfpclassify(d);
}

/// Count trailing zeroes at the end of bit field.
int xctz(uint64_t x)
{
  // If x == 0, that means all bits are zeroes.
  if (x == 0) {
    return 8 * sizeof(x);
  }

  // Use compiler builtin if possible.
#if defined(__clang__) || (defined(__GNUC__) && (__GNUC__ >= 4))
  return __builtin_ctzll(x);
#else
  int count = 0;
  // Set x's trailing zeroes to ones and zero the rest.
  x = (x ^ (x - 1)) >> 1;

  // Increment count until there are just zero bits remaining.
  while (x) {
    count++;
    x >>= 1;
  }

  return count;
#endif
}
