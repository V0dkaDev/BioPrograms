from collections import defaultdict


nucleotide_counts = {}
dinucleotide_counts = defaultdict(int)
trinucleotide_counts = defaultdict(int)

with open('example.fasta', 'r') as file:
    while True:
        one = file.readline().strip()
        two = file.readline().strip()
        three = file.readline()
        four = file.readline()
        
        if not one:
            break
        
        for nucleotide in two:
            nucleotide_counts[nucleotide] = nucleotide_counts.get(nucleotide, 0) + 1
        
        for i in range(len(two) - 1):
            dinucleotide = two[i:i+2]
            dinucleotide_counts[dinucleotide] += 1
        
        for i in range(len(two) - 2):
            trinucleotide = two[i:i+3]
            trinucleotide_counts[trinucleotide] += 1


print("Количество каждого нуклеотида:")
for nucleotide, count in sorted(nucleotide_counts.items()):
    print(f"{nucleotide}: {count}")

print("\nКоличество динуклеотидов:")
for dinucleotide, count in sorted(dinucleotide_counts.items()):
    print(f"{dinucleotide}: {count}")

print("\nКоличество тринуклеотидов:")
for trinucleotide, count in sorted(trinucleotide_counts.items()):
    print(f"{trinucleotide}: {count}")
