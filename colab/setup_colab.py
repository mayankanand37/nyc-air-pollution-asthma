"""Helper script for Colab: installs requirements and optionally downloads data.

Usage in Colab:
!python colab/setup_colab.py --raw-base https://raw.githubusercontent.com/mayankanand3007/nyc-air-pollution-asthma/main
"""
import argparse
import subprocess
import sys

def pip_install(url_or_file):
    cmd = [sys.executable, "-m", "pip", "install", "-r", url_or_file]
    subprocess.check_call(cmd)

def wget(url, out=None):
    cmd = ["wget", "-q", "-O", out if out else "-", url]
    subprocess.check_call(cmd)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--raw-base', help='Raw GitHub base URL (e.g. https://raw.githubusercontent.com/user/repo/main)')
    args = p.parse_args()
    if args.raw_base:
        req_url = args.raw_base.rstrip('/') + '/colab/colab_requirements.txt'
        print('Installing from', req_url)
        pip_install(req_url)
        data_url = args.raw_base.rstrip('/') + '/data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv'
        print('Downloading data from', data_url)
        try:
            wget(data_url, out='data_csv/SPARCS_asthma_hospitalizations_by_zip3_2010-2024.csv')
        except Exception:
            print('Warning: failed to download data; please download manually or mount Drive.')
    else:
        print('No --raw-base provided; installing local colab/colab_requirements.txt')
        pip_install('colab/colab_requirements.txt')
