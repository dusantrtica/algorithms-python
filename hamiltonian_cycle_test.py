def hamiltonian_cycle(graph):
    n = len(graph)
    visited = [False for _ in range(n)]

    def is_valid(vertex, next_move):
        if next_move in visited or graph[vertex][next_move]:
            return False

    start = graph[0][0]

    visited[0] = True
    hamiltonian_cycles = []
    path = [0 for _ in range(n)]

    # collect all hamiltonian cycles

    return True

def tsp(graph):
    hamiltonian_cycles = []


def test_hamiltonian_cycle_exist():
    graph = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    assert hamiltonian_cycle(graph) == True


def test_hamiltonian_cycle_not_exists():
    graph = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    assert hamiltonian_cycle(graph) == False
