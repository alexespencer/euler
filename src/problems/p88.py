import sys
import os
sys.path.insert(0, os.getcwd())

from euler import unique_product_from_factors, is_product_sum
from tqdm import tqdm

# A few things we can work out from this
# Given factors like {2, 5, 8} 2x5x8 = 80 we can always "pad" by n 'x1's where n = (80 - (2+5+8)) to get the number 1x1x....1x2x5x8 = 1+1+1+...+2+5+8

# The minimum product-sum for any k is larger or equal to k as for k of 6, 1+1+1+1+1+1 >= 6
# The maximum product-sum for any k is 2k, because we could always use 2xk then make up the rest with x1's as needed

factor_dict = {}

max_k = 12000

# Get a dict of n: all product combinations of n
product_perm_lookup = {}
for n in tqdm(range(2, (max_k+1)*2), desc="Generating product combinations"):
    product_perm_lookup[n] = unique_product_from_factors(factor_dict, n)

    # if current_prod < k:
    #     # print(f"K ({k}) is less than the product ({current_prod})")
    #     return False
    # if current_prod > 2 * k:
    #     # print(f"Product ({current_prod}) is more than twice K ({k})")
    #     return False

minimal_product_sum = {}
for k in tqdm(range(2, max_k+1), "Finding minimal product-sum for k"):
    # Finding minimal product-sum for k
    for current_prod, all_product_factors in product_perm_lookup.items():
        if k > current_prod > 2 * k:
            # Can't be a product-sum for this k
            continue

        if k in minimal_product_sum and current_prod > minimal_product_sum[k]:
            continue

        for product_factors in all_product_factors:
            # print(f"K: {k}, Current product: {current_prod}, Product factors: {product_factors}")
            # Check and if less than the current minimal, update
            if is_product_sum(current_prod, product_factors, k):
                if k not in minimal_product_sum or current_prod < minimal_product_sum[k]:
                    minimal_product_sum[k] = current_prod

sum_of_minimal_product_sum = sum(set(minimal_product_sum.values()))

print(f"The sum of all the minimal product-sum numbers for 2≤k≤{max_k} is {sum_of_minimal_product_sum}")

