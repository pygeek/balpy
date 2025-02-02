from decimal import Decimal


BONE = Decimal("1")
MIN_FEE = Decimal("0.000001")
MAX_FEE = Decimal("0.1")
INIT_POOL_SUPPLY = BONE * Decimal("100")
MIN_BOUND_TOKENS = 2
MAX_BOUND_TOKENS = 8
AMPLIFICATION_PARAMETER = Decimal("200")
MIN_WEIGHT = 0.01
_MAX_WEIGHTED_TOKENS = 100
_MAX_IN_RATIO = 0.3
_MAX_OUT_RATIO = 0.3
_MAX_INVARIANT_RATIO = 3
_MIN_INVARIANT_RATIO = 0.7
