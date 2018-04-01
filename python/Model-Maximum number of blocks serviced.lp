\* Park Location Model: Maximum number of blocks serviced *\
Maximize
Maximum_number_of_blocks_serviced: z10 + z11 + z13 + z14 + z16 + z17 + z18
 + z2 + z20 + z22 + z23 + z24 + z25 + z4 + z6 + z7 + z8 + z9
Subject To
Can_only_build_1_park(s): y1 + y12 + y15 + y19 + y21 + y3 <= 1
If_a_park_serving_lot_10_is_picked_then_lot_10_must_be_serviced: - y15 + z10
 >= 0
If_a_park_serving_lot_11_is_picked_then_lot_11_must_be_serviced: - y12 + z11
 >= 0
If_a_park_serving_lot_13_is_picked_then_lot_13_must_be_serviced: - y12 - y19
 + 2 z13 >= 0
If_a_park_serving_lot_14_is_picked_then_lot_14_must_be_serviced: - y15 - y19
 + 2 z14 >= 0
If_a_park_serving_lot_16_is_picked_then_lot_16_must_be_serviced: - y12 - y21
 + 2 z16 >= 0
If_a_park_serving_lot_17_is_picked_then_lot_17_must_be_serviced: - y12 - y21
 + 2 z17 >= 0
If_a_park_serving_lot_18_is_picked_then_lot_18_must_be_serviced: - y12 - y19
 + 2 z18 >= 0
If_a_park_serving_lot_20_is_picked_then_lot_20_must_be_serviced: - y15 - y19
 + 2 z20 >= 0
If_a_park_serving_lot_22_is_picked_then_lot_22_must_be_serviced: - y21 + z22
 >= 0
If_a_park_serving_lot_23_is_picked_then_lot_23_must_be_serviced: - y19 + z23
 >= 0
If_a_park_serving_lot_24_is_picked_then_lot_24_must_be_serviced: - y19 + z24
 >= 0
If_a_park_serving_lot_25_is_picked_then_lot_25_must_be_serviced: - y19 + z25
 >= 0
If_a_park_serving_lot_2_is_picked_then_lot_2_must_be_serviced: - y1 - y3
 + 2 z2 >= 0
If_a_park_serving_lot_4_is_picked_then_lot_4_must_be_serviced: - y3 + z4 >= 0
If_a_park_serving_lot_6_is_picked_then_lot_6_must_be_serviced: - y1 - y12
 + 2 z6 >= 0
If_a_park_serving_lot_7_is_picked_then_lot_7_must_be_serviced: - y1 - y12 - y3
 + 3 z7 >= 0
If_a_park_serving_lot_8_is_picked_then_lot_8_must_be_serviced: - y12 - y3
 + 2 z8 >= 0
If_a_park_serving_lot_9_is_picked_then_lot_9_must_be_serviced: - y15 - y3
 + 2 z9 >= 0
If_lot_10_is_serviced_at_least_one_park_is_built: y15 - z10 >= 0
If_lot_11_is_serviced_at_least_one_park_is_built: y12 - z11 >= 0
If_lot_13_is_serviced_at_least_one_park_is_built: y12 + y19 - z13 >= 0
If_lot_14_is_serviced_at_least_one_park_is_built: y15 + y19 - z14 >= 0
If_lot_16_is_serviced_at_least_one_park_is_built: y12 + y21 - z16 >= 0
If_lot_17_is_serviced_at_least_one_park_is_built: y12 + y21 - z17 >= 0
If_lot_18_is_serviced_at_least_one_park_is_built: y12 + y19 - z18 >= 0
If_lot_20_is_serviced_at_least_one_park_is_built: y15 + y19 - z20 >= 0
If_lot_22_is_serviced_at_least_one_park_is_built: y21 - z22 >= 0
If_lot_23_is_serviced_at_least_one_park_is_built: y19 - z23 >= 0
If_lot_24_is_serviced_at_least_one_park_is_built: y19 - z24 >= 0
If_lot_25_is_serviced_at_least_one_park_is_built: y19 - z25 >= 0
If_lot_2_is_serviced_at_least_one_park_is_built: y1 + y3 - z2 >= 0
If_lot_4_is_serviced_at_least_one_park_is_built: y3 - z4 >= 0
If_lot_6_is_serviced_at_least_one_park_is_built: y1 + y12 - z6 >= 0
If_lot_7_is_serviced_at_least_one_park_is_built: y1 + y12 + y3 - z7 >= 0
If_lot_8_is_serviced_at_least_one_park_is_built: y12 + y3 - z8 >= 0
If_lot_9_is_serviced_at_least_one_park_is_built: y15 + y3 - z9 >= 0
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
