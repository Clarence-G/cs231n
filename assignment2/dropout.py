def dropout_forward(x, dropout_param):
    p, mode = dropout_param['p'], dropout_param['mode']
    if 'seed' in dropout_param:  
        np.random.seed(dropout_param['seed'])

    mask = None
    out = None
    if mode == 'train':    
        mask = (np.random.rand(*x.shape) < p) / p    
        out = x * mask
    elif mode == 'test':    
        out = x

    cache = (dropout_param, mask)
    out = out.astype(x.dtype, copy=False)

    return out, cache


def dropout_backward(dout, cache):
    dropout_param, mask = cache
    mode = dropout_param['mode']
    dx = None

    if mode == 'train':    
        dx = dout * mask
    elif mode == 'test':    
        dx = dout

    return dx
