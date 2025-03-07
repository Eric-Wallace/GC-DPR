#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import importlib

"""
 'Router'-like set of methods for component initialization with lazy imports 
"""


def init_hf_bert_biencoder(args, **kwargs):
    if importlib.util.find_spec("transformers") is None:
        raise RuntimeError('Please install transformers lib')
    from .hf_models import get_bert_biencoder_components
    return get_bert_biencoder_components(args, **kwargs)


def init_hf_bert_tenzorizer(args, **kwargs):
    if importlib.util.find_spec("transformers") is None:
        raise RuntimeError('Please install transformers lib')
    from .hf_models import get_bert_tensorizer
    return get_bert_tensorizer(args)


def init_hf_esm_biencoder(args, **kwargs):
    if importlib.util.find_spec("transformers") is None:
        raise RuntimeError('Please install transformers lib')
    from .hf_models import get_esm_biencoder_components
    return get_esm_biencoder_components(args, **kwargs)


def init_hf_esm_tenzorizer(args, **kwargs):
    if importlib.util.find_spec("transformers") is None:
        raise RuntimeError('Please install transformers lib')
    from .hf_models import get_esm_tensorizer
    return get_esm_tensorizer(args)


def init_hf_roberta_tenzorizer(args, **kwargs):
    if importlib.util.find_spec("transformers") is None:
        raise RuntimeError('Please install transformers lib')
    from .hf_models import get_roberta_tensorizer
    return get_roberta_tensorizer(args)


BIENCODER_INITIALIZERS = {
    'hf_bert': init_hf_bert_biencoder,
    'hf_esm': init_hf_esm_biencoder,
}

TENSORIZER_INITIALIZERS = {
    'hf_bert': init_hf_bert_tenzorizer,
    'hf_esm': init_hf_esm_tenzorizer,
    'hf_roberta': init_hf_roberta_tenzorizer,
}

def init_comp(initializers_dict, type, args, **kwargs):
    if type in initializers_dict:
        return initializers_dict[type](args, **kwargs)
    else:
        raise RuntimeError('unsupported model type: {}'.format(type))


def init_biencoder_components(encoder_type: str, args, **kwargs):
    return init_comp(BIENCODER_INITIALIZERS, encoder_type, args, **kwargs)

def init_tenzorizer(encoder_type: str, args, **kwargs):
    return init_comp(TENSORIZER_INITIALIZERS, encoder_type, args, **kwargs)
