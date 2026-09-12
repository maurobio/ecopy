import unittest
import numpy as np
import pandas as pd

import ecopy as ep


class TestModernEcoPy(unittest.TestCase):

    def setUp(self):
        self.abund = np.array([
            [5, 2, 1, 3],
            [4, 3, 2, 2],
            [2, 5, 3, 1],
            [1, 3, 5, 2],
            [3, 1, 4, 5],
            [2, 4, 2, 4],
        ], dtype=int)
        self.groups = np.array(["A", "A", "A", "B", "B", "B"])
        self.dist = ep.distance(self.abund, method="bray")
        self.env = pd.DataFrame({
            "temperature": [10., 12., 14., 16., 18., 20.],
            "pH": [7., 6.8, 7.4, 6.7, 7.5, 6.9],
        })
        self.traits = pd.DataFrame({
            "size": [1., 2., 3., 4.],
            "leaf_area": [4., 3., 2., 1.],
        })

    def test_import_and_version(self):
        self.assertTrue(ep.__version__.startswith("0.2.0"))

    def test_transform_and_distance(self):
        transformed = ep.transform(self.abund, method="total", axis=1)
        self.assertEqual(transformed.shape, self.abund.shape)
        np.testing.assert_allclose(transformed.sum(axis=1), 1.0)
        self.assertEqual(self.dist.shape, (6, 6))

    def test_diversity(self):
        result = ep.diversity(self.abund, method="shannon")
        self.assertEqual(result.shape, (6,))
        self.assertTrue(np.all(np.isfinite(result)))

    def test_rarefy(self):
        result = ep.rarefy(self.abund[:2], method="rarefy", size=5)
        self.assertEqual(result.shape, (2,))
        self.assertTrue(np.all(np.isfinite(result)))

    def test_ordination(self):
        pca = ep.pca(self.abund)
        ca = ep.ca(self.abund)
        pcoa = ep.pcoa(self.dist)
        mds = ep.MDS(self.dist, ntry=2, maxiter=100)
        self.assertEqual(pca.scores.shape[0], 6)
        self.assertEqual(ca.siteScores.shape[0], 6)
        self.assertEqual(pcoa.U.shape[0], 6)
        self.assertEqual(mds.scores.shape[0], 6)

    def test_isotonic(self):
        fit = ep.isotonic([3., 1., 2.])
        self.assertTrue(np.all(np.diff(fit.prediction) >= -1e-12))

    def test_mantel_and_anosim(self):
        mantel = ep.Mantel(self.dist, self.dist, nperm=9)
        anosim = ep.anosim(self.dist, self.groups, nperm=9)
        self.assertTrue(np.isfinite(mantel.r_obs))
        self.assertTrue(np.isfinite(anosim.R_obs1))

    def test_simper(self):
        result = ep.simper(pd.DataFrame(self.abund), self.groups)
        self.assertGreater(len(result), 0)
        self.assertIn("sp_pct", result.columns)

    def test_constrained_ordination(self):
        rda = ep.rda(self.abund, self.env)
        cca = ep.cca(self.abund, self.env)
        ccor = ep.ccor(self.env, pd.DataFrame(self.abund[:, :2]))
        self.assertGreater(len(rda.RDA_evals), 0)
        self.assertGreater(len(cca.evals), 0)
        self.assertGreater(len(ccor.evals), 0)

    def test_rlq_and_fourthcorner(self):
        rlq = ep.rlq(self.env, pd.DataFrame(self.abund), self.traits)
        fc = ep.corner4(self.env, self.abund, self.traits, nperm=9)
        self.assertGreater(len(rlq.evals), 0)
        self.assertTrue(hasattr(fc, "summary"))

    def test_procrustes_and_bioenv(self):
        proc = ep.procrustes_test(self.abund.astype(float),
                                  self.abund.astype(float), nperm=9)
        bio = ep.bioenv(self.dist, self.env)
        self.assertTrue(np.isfinite(proc.m12_obs))
        self.assertGreater(len(bio), 0)


if __name__ == "__main__":
    unittest.main()
