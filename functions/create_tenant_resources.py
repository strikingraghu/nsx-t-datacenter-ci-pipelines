import os
import json


def create_edge_params():
    dns_domain = os.getenv('dns_domain_int')
    edge_specs = os.getenv('tenant_edge_clusters_int')
    tenant_edge_clusters = json.loads(edge_specs)

    with open('tenant_edges', 'w') as edge_output_file:
        edge_output_file.write('[tenant_edge_nodes]\n')
        for edge_cluster in tenant_edge_clusters:
            edge_ips = edge_cluster['edge_ips'].split(',')
            for i in range(len(edge_ips)):
                item_name = "%s-%s" % (edge_cluster['edge_hostname_prefix'], i+1)
                hostname = item_name + dns_domain
                transport_node_name = "%s-%s" % (edge_cluster['edge_transport_node_prefix'], i+1)
                edge_string = item_name + ' ' + edge_cluster['edge_ips'][i] + ' ' + hostname
                edge_string += ' ' + edge_cluster['edge_default_gateway']
                edge_string += ' ' + str(edge_cluster['edge_ip_prefix_length'])
                edge_string += ' ' + transport_node_name
                edge_string += ' ' + edge_cluster['vc_cluster_for_edge']
                edge_string += ' ' + edge_cluster['vc_datacenter_for_edge']
                edge_string += ' ' + edge_cluster['vc_datastore_for_edge']
                edge_string += ' ' + edge_cluster['vc_management_network_for_edge']
                edge_string += ' ' + edge_cluster['vc_overlay_network_for_edge']
                edge_string += ' ' + edge_cluster['vc_uplink_network_for_edge']
                edge_output_file.write(edge_string + '\n')


def create_t0_params():
    t0_specs = os.getenv('tenant_t0s_int')
    tenant_t0s = json.loads(t0_specs)


def main():
    create_edge_params()
    create_t0_params()


if __name__ == '__main__':
    main()
