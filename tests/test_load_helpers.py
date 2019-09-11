"""Test vt_graph_api.load.helpers module."""


import vt_graph_api.load.helpers


def test_range_ip():
  start_ip = "1.2.3.4"
  end_ip = "1.2.3.20"
  ips = [
      "1.2.3.4", "1.2.3.5", "1.2.3.6", "1.2.3.7", "1.2.3.8", "1.2.3.9",
      "1.2.3.10", "1.2.3.11", "1.2.3.12", "1.2.3.13", "1.2.3.14", "1.2.3.15",
      "1.2.3.16", "1.2.3.17", "1.2.3.18", "1.2.3.19", "1.2.3.20"
  ]
  assert ips == vt_graph_api.load.helpers.range_ips(start_ip, end_ip)
