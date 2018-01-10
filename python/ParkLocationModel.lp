\* Park Location Problem *\
Maximize
the_maximum_number_of_blocks_serviced: z10 + z11 + z13 + z14 + z16 + z17 + z18
 + z2 + z20 + z22 + z23 + z24 + z25 + z4 + z6 + z7 + z8 + z9
Subject To
Ensures_if_lot_10_is_serviced_at_least_one_park_is_built: y15 - z10 >= 0
Ensures_if_lot_11_is_serviced_at_least_one_park_is_built: y12 - z11 >= 0
Ensures_if_lot_13_is_serviced_at_least_one_park_is_built: y12 + y19 - z13 >= 0
Ensures_if_lot_14_is_serviced_at_least_one_park_is_built: y15 + y19 - z14 >= 0
Ensures_if_lot_16_is_serviced_at_least_one_park_is_built: y12 + y21 - z16 >= 0
Ensures_if_lot_17_is_serviced_at_least_one_park_is_built: y12 + y21 - z17 >= 0
Ensures_if_lot_18_is_serviced_at_least_one_park_is_built: y12 + y19 - z18 >= 0
Ensures_if_lot_20_is_serviced_at_least_one_park_is_built: y15 + y19 - z20 >= 0
Ensures_if_lot_22_is_serviced_at_least_one_park_is_built: y21 - z22 >= 0
Ensures_if_lot_23_is_serviced_at_least_one_park_is_built: y19 - z23 >= 0
Ensures_if_lot_24_is_serviced_at_least_one_park_is_built: y19 - z24 >= 0
Ensures_if_lot_25_is_serviced_at_least_one_park_is_built: y19 - z25 >= 0
Ensures_if_lot_2_is_serviced_at_least_one_park_is_built: y1 + y3 - z2 >= 0
Ensures_if_lot_4_is_serviced_at_least_one_park_is_built: y3 - z4 >= 0
Ensures_if_lot_6_is_serviced_at_least_one_park_is_built: y1 + y12 - z6 >= 0
Ensures_if_lot_7_is_serviced_at_least_one_park_is_built: y1 + y12 + y3 - z7
 >= 0
Ensures_if_lot_8_is_serviced_at_least_one_park_is_built: y12 + y3 - z8 >= 0
Ensures_if_lot_9_is_serviced_at_least_one_park_is_built: y15 + y3 - z9 >= 0
Binaries
y1
y12
y15
y19
y21
y3
z10
z11
z13
z14
z16
z17
z18
z2
z20
z22
z23
z24
z25
z4
z6
z7
z8
z9
End
