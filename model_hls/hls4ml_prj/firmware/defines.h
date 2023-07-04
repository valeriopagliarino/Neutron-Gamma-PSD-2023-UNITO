#ifndef DEFINES_H_
#define DEFINES_H_

#include "ap_fixed.h"
#include "ap_int.h"
#include "nnet_utils/nnet_types.h"
#include <cstddef>
#include <cstdio>

// hls-fpga-machine-learning insert numbers
#define N_INPUT_1_1 240
#define N_INPUT_2_1 1
#define N_OUTPUTS_2 235
#define N_FILT_2 4
#define N_OUTPUTS_2 235
#define N_FILT_2 4
#define N_OUTPUTS_4 117
#define N_FILT_4 4
#define N_OUTPUTS_5 112
#define N_FILT_5 8
#define N_OUTPUTS_5 112
#define N_FILT_5 8
#define N_OUTPUTS_7 56
#define N_FILT_7 8
#define N_SIZE_0_8 448
#define N_LAYER_9 34
#define N_LAYER_9 34
#define N_LAYER_11 1
#define N_LAYER_11 1

// hls-fpga-machine-learning insert layer-precision
typedef ap_fixed<16,6> input_t;
typedef ap_fixed<16,6> model_default_t;
typedef ap_fixed<16,6> layer2_t;
typedef ap_fixed<16,6> layer3_t;
typedef ap_fixed<18,8> conv1d_2_relu_table_t;
typedef ap_fixed<16,6> layer4_t;
typedef ap_fixed<16,6> layer5_t;
typedef ap_fixed<16,6> layer6_t;
typedef ap_fixed<18,8> conv1d_3_relu_table_t;
typedef ap_fixed<16,6> layer7_t;
typedef ap_fixed<16,6> layer9_t;
typedef ap_uint<1> layer9_index;
typedef ap_fixed<16,6> layer10_t;
typedef ap_fixed<18,8> dense_1_relu_table_t;
typedef ap_fixed<16,6> layer11_t;
typedef ap_uint<1> layer11_index;
typedef ap_fixed<16,6> result_t;
typedef ap_fixed<18,8> dense_out_sigmoid_table_t;

#endif
