#!/usr/bin/env bash

models/train.sh crf_cnn_characters_only exists_ru models/crf/characters_only/cnn/lstm.jsonnet
models/train.sh crf_cnn_characters_only_bidir exists_ru models/crf/characters_only/cnn/lstm_bidir.jsonnet
models/train.sh crf_cnn_characters_only_multi_head_self_attention exists_ru models/crf/characters_only/cnn/multi_head_self_attention.jsonnet
models/train.sh crf_cnn_characters_only_bidirectional_language_model_transformer exists_ru models/crf/characters_only/cnn/bidirectional_language_model_transformer.jsonnet
models/train.sh crf_cnn_characters_only_qanet_encoder exists_ru models/crf/characters_only/cnn/qanet_encoder.jsonnet

models/train.sh crf_cnn_characters_only_stacked_bidirectional_lstm exists_ru models/crf/characters_only/cnn/stacked_bidirectional_lstm.jsonnet
models/train.sh crf_cnn_characters_only_stacked_self_attention exists_ru models/crf/characters_only/cnn/stacked_self_attention.jsonnet
models/train.sh crf_cnn_characters_only_alternating_lstm exists_ru models/crf/characters_only/cnn/alternating_lstm.jsonnet
models/train.sh crf_cnn_characters_only_alternating_lstm exists_ru models/crf/characters_only/cnn/alternating_lstm.jsonnet
models/train.sh crf_cnn_characters_only_augmented_lstm exists_ru models/crf/characters_only/cnn/augmented_lstm.jsonnet