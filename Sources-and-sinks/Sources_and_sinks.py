def find_sources_and_sinks(n, adj_matrix):
    sources = []
    sinks = []
    
   
    for i in range(n):
        is_source = True
        for j in range(n):
            if adj_matrix[j][i] == 1:
                is_source = False
                break
        if is_source:
            sources.append(i + 1)
    
    # Check for sinks
    for i in range(n):
        is_sink = True
        for j in range(n):
            if adj_matrix[i][j] == 1:
                is_sink = False
                break
        if is_sink:
            sinks.append(i + 1)
    
    return sources, sinks

# Reading input
n = int(input())
adj_matrix = []
for _ in range(n):
    adj_matrix.append(list(map(int, input().split())))

sources, sinks = find_sources_and_sinks(n, adj_matrix)

# Output the results
print(len(sources), ' '.join(map(str, sources)))
print(len(sinks), ' '.join(map(str, sinks)))