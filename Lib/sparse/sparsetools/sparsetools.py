# This file was created automatically by SWIG 1.3.28.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _sparsetools
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types




def csrtocsc(*args):
    """
    csrtocsc(int n_row, int n_col, int Ap, int Aj, float Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bi, std::vector<(float)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, double Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bi, std::vector<(double)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(long double)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cfloat)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cdouble)> Bx)
    csrtocsc(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_clongdouble)> Bx)
    """
    return _sparsetools.csrtocsc(*args)

def csctocsr(*args):
    """
    csctocsr(int n_row, int n_col, int Ap, int Ai, float Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, double Ax, std::vector<(int)> Bp, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, long double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(long double)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    csctocsr(int n_row, int n_col, int Ap, int Ai, npy_clongdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_clongdouble)> Bx)
    """
    return _sparsetools.csctocsr(*args)

def csrtocoo(*args):
    """
    csrtocoo(int n_row, int n_col, int Ap, int Aj, float Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, double Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(long double)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    csrtocoo(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_clongdouble)> Bx)
    """
    return _sparsetools.csrtocoo(*args)

def cootocsr(*args):
    """
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, float Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(float)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(double)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, long double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(long double)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    cootocsr(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_clongdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bj, 
        std::vector<(npy_clongdouble)> Bx)
    """
    return _sparsetools.cootocsr(*args)

def csctocoo(*args):
    """
    csctocoo(int n_row, int n_col, int Ap, int Ai, float Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(float)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, double Ax, std::vector<(int)> Bi, 
        std::vector<(int)> Bj, std::vector<(double)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, long double Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(long double)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cfloat)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_cdouble)> Bx)
    csctocoo(int n_row, int n_col, int Ap, int Ai, npy_clongdouble Ax, 
        std::vector<(int)> Bi, std::vector<(int)> Bj, 
        std::vector<(npy_clongdouble)> Bx)
    """
    return _sparsetools.csctocoo(*args)

def cootocsc(*args):
    """
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, float Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(float)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(double)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, long double Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(long double)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cfloat Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cfloat)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_cdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_cdouble)> Bx)
    cootocsc(int n_row, int n_col, int NNZ, int Ai, int Aj, npy_clongdouble Ax, 
        std::vector<(int)> Bp, std::vector<(int)> Bi, 
        std::vector<(npy_clongdouble)> Bx)
    """
    return _sparsetools.cootocsc(*args)

def csrplcsr(*args):
    """
    csrplcsr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csrplcsr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csrplcsr(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        int Bp, int Bj, long double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(long double)> Cx)
    csrplcsr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csrplcsr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    csrplcsr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        int Bp, int Bj, npy_clongdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_clongdouble)> Cx)
    """
    return _sparsetools.csrplcsr(*args)

def cscplcsc(*args):
    """
    cscplcsc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    cscplcsc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    cscplcsc(int n_row, int n_col, int Ap, int Ai, long double Ax, 
        int Bp, int Bi, long double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(long double)> Cx)
    cscplcsc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    cscplcsc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    cscplcsc(int n_row, int n_col, int Ap, int Ai, npy_clongdouble Ax, 
        int Bp, int Bi, npy_clongdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_clongdouble)> Cx)
    """
    return _sparsetools.cscplcsc(*args)

def csrmucsr(*args):
    """
    csrmucsr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        int Bp, int Bj, long double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(long double)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    csrmucsr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        int Bp, int Bj, npy_clongdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_clongdouble)> Cx)
    """
    return _sparsetools.csrmucsr(*args)

def cscmucsc(*args):
    """
    cscmucsc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, long double Ax, 
        int Bp, int Bi, long double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(long double)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    cscmucsc(int n_row, int n_col, int Ap, int Ai, npy_clongdouble Ax, 
        int Bp, int Bi, npy_clongdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_clongdouble)> Cx)
    """
    return _sparsetools.cscmucsc(*args)

def csrmux(*args):
    """
    csrmux(int n_row, int n_col, int Ap, int Aj, float Ax, float Xx, 
        std::vector<(float)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, double Ax, double Xx, 
        std::vector<(double)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        long double Xx, std::vector<(long double)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        npy_cfloat Xx, std::vector<(npy_cfloat)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        npy_cdouble Xx, std::vector<(npy_cdouble)> Yx)
    csrmux(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        npy_clongdouble Xx, std::vector<(npy_clongdouble)> Yx)
    """
    return _sparsetools.csrmux(*args)

def cscmux(*args):
    """
    cscmux(int n_row, int n_col, int Ap, int Ai, float Ax, float Xx, 
        std::vector<(float)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, double Ax, double Xx, 
        std::vector<(double)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, long double Ax, 
        long double Xx, std::vector<(long double)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        npy_cfloat Xx, std::vector<(npy_cfloat)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        npy_cdouble Xx, std::vector<(npy_cdouble)> Yx)
    cscmux(int n_row, int n_col, int Ap, int Ai, npy_clongdouble Ax, 
        npy_clongdouble Xx, std::vector<(npy_clongdouble)> Yx)
    """
    return _sparsetools.cscmux(*args)

def csrelmulcsr(*args):
    """
    csrelmulcsr(int n_row, int n_col, int Ap, int Aj, float Ax, int Bp, 
        int Bj, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(float)> Cx)
    csrelmulcsr(int n_row, int n_col, int Ap, int Aj, double Ax, int Bp, 
        int Bj, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(double)> Cx)
    csrelmulcsr(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        int Bp, int Bj, long double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(long double)> Cx)
    csrelmulcsr(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        int Bp, int Bj, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cfloat)> Cx)
    csrelmulcsr(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        int Bp, int Bj, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_cdouble)> Cx)
    csrelmulcsr(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        int Bp, int Bj, npy_clongdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Cj, std::vector<(npy_clongdouble)> Cx)
    """
    return _sparsetools.csrelmulcsr(*args)

def cscelmulcsc(*args):
    """
    cscelmulcsc(int n_row, int n_col, int Ap, int Ai, float Ax, int Bp, 
        int Bi, float Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(float)> Cx)
    cscelmulcsc(int n_row, int n_col, int Ap, int Ai, double Ax, int Bp, 
        int Bi, double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(double)> Cx)
    cscelmulcsc(int n_row, int n_col, int Ap, int Ai, long double Ax, 
        int Bp, int Bi, long double Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(long double)> Cx)
    cscelmulcsc(int n_row, int n_col, int Ap, int Ai, npy_cfloat Ax, 
        int Bp, int Bi, npy_cfloat Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cfloat)> Cx)
    cscelmulcsc(int n_row, int n_col, int Ap, int Ai, npy_cdouble Ax, 
        int Bp, int Bi, npy_cdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_cdouble)> Cx)
    cscelmulcsc(int n_row, int n_col, int Ap, int Ai, npy_clongdouble Ax, 
        int Bp, int Bi, npy_clongdouble Bx, std::vector<(int)> Cp, 
        std::vector<(int)> Ci, std::vector<(npy_clongdouble)> Cx)
    """
    return _sparsetools.cscelmulcsc(*args)

def spdiags(*args):
    """
    spdiags(int n_row, int n_col, int n_diag, int offsets, float diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(float)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, double diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(double)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, long double diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(long double)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, npy_cfloat diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(npy_cfloat)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, npy_cdouble diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(npy_cdouble)> Ax)
    spdiags(int n_row, int n_col, int n_diag, int offsets, npy_clongdouble diags, 
        std::vector<(int)> Ap, std::vector<(int)> Ai, 
        std::vector<(npy_clongdouble)> Ax)
    """
    return _sparsetools.spdiags(*args)

def csrtodense(*args):
    """
    csrtodense(int n_row, int n_col, int Ap, int Aj, float Ax, float Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, double Ax, double Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, long double Ax, 
        long double Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, npy_cfloat Ax, 
        npy_cfloat Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, npy_cdouble Ax, 
        npy_cdouble Mx)
    csrtodense(int n_row, int n_col, int Ap, int Aj, npy_clongdouble Ax, 
        npy_clongdouble Mx)
    """
    return _sparsetools.csrtodense(*args)

def densetocsr(*args):
    """
    densetocsr(int n_row, int n_col, float Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(float)> Ax)
    densetocsr(int n_row, int n_col, double Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(double)> Ax)
    densetocsr(int n_row, int n_col, long double Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(long double)> Ax)
    densetocsr(int n_row, int n_col, npy_cfloat Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(npy_cfloat)> Ax)
    densetocsr(int n_row, int n_col, npy_cdouble Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(npy_cdouble)> Ax)
    densetocsr(int n_row, int n_col, npy_clongdouble Mx, std::vector<(int)> Ap, 
        std::vector<(int)> Aj, std::vector<(npy_clongdouble)> Ax)
    """
    return _sparsetools.densetocsr(*args)

