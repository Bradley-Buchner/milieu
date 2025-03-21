"""
Functions for generating and managing embeddings.
"""

import numpy as np


def load_embeddings(embeddings_path, network): 
    """ Builds a numpy matrix for a node embedding encoded in the embeddingf ile
    passed in. Row indices are given by protein_to_node dictionary passed in. 
    @param embedding_filename (string)
    @param network (Network)
    @returns embeddings (np.array)
    """
    with open(embeddings_path) as embedding_file:
        # get  
        line = embedding_file.readline()
        n_nodes, n_dim = map(int, line.split(" "))
        embeddings = np.empty((len(network), n_dim))

        for index in range(n_nodes):
            line = embedding_file.readline()
            line_elements = line.split(" ")
            protein = int(line_elements[0])

            if protein not in network.protein_to_node: 
                continue  
                
            node_embedding = list(map(float, line_elements[1:]))
            embeddings[network.get_node(protein), :] = node_embedding

    return embeddings


def write_embeddings(embeddings, embeddings_path, network):
    """
    @param embeddings (np.array)
    @param embeddings_path (string)
    @param network (Network)
    """
    with open(embeddings_path, 'w') as embedding_file:
        n_nodes, n_dim = embeddings.shape
        embedding_file.write(f"{n_nodes} {n_dim}\n")
        for node in range(n_nodes):
            protein = network.get_protein(node)
            embedding = " ".join(map(str, list(embeddings[node, :])))
            line = f"{protein} {embedding}\n"
            embedding_file.write(line)
    