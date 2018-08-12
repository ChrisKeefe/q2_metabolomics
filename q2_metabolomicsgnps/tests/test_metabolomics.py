import unittest
import io
import os
import csv


from q2_metabolomicsgnps._method import _create_table_from_task

class MetabolomicsTestCase(unittest.TestCase):

    #def test_gnps(self):
    #    gnps_clustering("data/manifest.tsv", "qiime2test", "qiime2test")

    def test_featureloading(self):
        manifest = "data/manifest.tsv"
        sid_map = {}
        with open(manifest) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sid = row["sample-id"]
                filepath = row["filepath"]
                fileidentifier = os.path.basename(os.path.splitext(filepath)[0])
                sid_map[fileidentifier] = sid

        task_id = "cde9c128ec0c48a58e650279f1735dbc"

        _create_table_from_task(task_id, sid_map)


if __name__ == '__main__':
    unittest.main()
