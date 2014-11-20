#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Testing suite for ARG class.

"""
from __future__ import print_function, division

import unittest as ut
import numpy as np

import ARG.arg as arg

__author__ = "Stanislav Khrapov"
__email__ = "khrapovs@gmail.com"
__status__ = "Development"


class ARGTestCase(ut.TestCase):

    def test_param_class(self):
        """Test parameter class."""

        param = arg.ARGparams()

        self.assertIsInstance(param.scale, float)
        self.assertIsInstance(param.rho, float)
        self.assertIsInstance(param.delta, float)
        self.assertIsInstance(param.beta, float)

    def test_uncond_moments(self):
        """Test unconditional moments of the ARG model."""

        argmodel = arg.ARG()

        self.assertIsInstance(argmodel.umean(), float)
        self.assertIsInstance(argmodel.uvar(), float)
        self.assertIsInstance(argmodel.ustd(), float)

        # TODO : test using symbolic library
        # that these moments coincide with derivatives of a, b, c


    def test_abc_functions(self):
        """Test functions a, b, c of ARG model."""

        argmodel = arg.ARG()
        uarg = np.linspace(-50, 100, 100)

        self.assertIsInstance(argmodel.afun(uarg), np.ndarray)
        self.assertIsInstance(argmodel.bfun(uarg), np.ndarray)
        self.assertIsInstance(argmodel.cfun(uarg), np.ndarray)

        self.assertEqual(uarg.shape, argmodel.afun(uarg).shape)
        self.assertEqual(uarg.shape, argmodel.bfun(uarg).shape)
        self.assertEqual(uarg.shape, argmodel.cfun(uarg).shape)

    def test_simulations(self):
        """Test simulation of ARG model."""

        argmodel = arg.ARG()

        self.assertIsInstance(argmodel.vsim(), np.ndarray)
        self.assertIsInstance(argmodel.vsim2(), np.ndarray)

        nsim, nobs = 1, 1
        shape = (nsim, nobs)
        self.assertEqual(argmodel.vsim(nsim=nsim, nobs=nobs).shape, shape)
        self.assertEqual(argmodel.vsim2(nsim=nsim, nobs=nobs).shape, shape)
        self.assertEqual(argmodel.vsim_last(nsim=nsim, nobs=nobs).shape,
                         (nsim, ))

        nsim, nobs = 2, 2
        shape = (nsim, nobs)
        self.assertEqual(argmodel.vsim(nsim=nsim, nobs=nobs).shape, shape)
        self.assertEqual(argmodel.vsim2(nsim=nsim, nobs=nobs).shape, shape)
        self.assertEqual(argmodel.vsim_last(nsim=nsim, nobs=nobs).shape,
                         (nsim, ))


if __name__ == '__main__':
    ut.main()