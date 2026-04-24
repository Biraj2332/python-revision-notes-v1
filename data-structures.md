# 📘 Data Structures — Comprehensive Reference Guide

> **Scope:** Computer Science fundamentals, interview preparation, and system design.  
> **Level:** Beginner → Research-grade.  
> **Language examples:** Python 3.

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Data Structure Architecture](#2-data-structure-architecture)
3. [Built-in Data Structures](#3-built-in-data-structures)
4. [User-Defined Data Structures](#4-user-defined-data-structures)
5. [Comparative Architecture](#5-comparative-architecture)
6. [Data Structures in Algorithms](#6-data-structures-in-algorithms)
7. [Real-World System Design Mapping](#7-real-world-system-design-mapping)
8. [Implementation Section (Python)](#8-implementation-section-python)
9. [Visualization Section](#9-visualization-section)
10. [Research & References](#10-research--references)
11. [Practice & Interview Questions](#11-practice--interview-questions)
12. [Summary + Revision Notes](#12-summary--revision-notes)

---

# 1. Introduction

## 1.1 Formal Definition

A **data structure** is a systematic way of organizing, storing, and managing data in a computer's memory so that it can be accessed and modified efficiently. Formally:

> *"A data structure is a particular way of storing and organizing data in a computer so that it can be used efficiently. Different data structures are suited to different kinds of applications, and some are highly specialized to specific tasks."*  
> — Knuth, *The Art of Computer Programming*

From a theoretical computer science perspective, a data structure is defined by:

1. **A collection of data values** — the domain of the structure.
2. **The relationships among those values** — how elements relate to each other.
3. **The operations that can be applied** — the interface (ADT contract).

In essence, a data structure is the physical realization of an **Abstract Data Type (ADT)**.

## 1.2 Why Data Organization Matters

Raw data stored without structure leads to:

| Problem | Consequence |
|---|---|
| Linear search through RAM | O(n) lookup every time |
| No locality of reference | Cache misses, slow I/O |
| No ordering guarantees | Sorting required before every query |
| Redundant storage | Wasted memory, slow traversal |

Well-chosen data structures reduce time complexity, improve cache performance, minimize memory footprint, and make algorithms elegant. The choice of data structure is often the single most impactful engineering decision in a system.

> *Data structures organize data for efficient processing and representation of real-world relationships. The right structure can reduce an O(n²) algorithm to O(n log n) simply by reorganizing memory.*  
> — Adapted from ScienceDirect (2020)

## 1.3 Classification

### Primitive vs Non-Primitive

```
Data Types
├── Primitive (directly supported by hardware/CPU)
│   ├── int
│   ├── float
│   ├── char
│   └── bool
└── Non-Primitive (composed from primitives)
    ├── Built-in / Language-provided
    │   ├── List, Tuple, Set, Dict, Array
    └── User-Defined
        ├── Stack, Queue, Linked List, Tree, Graph
```

**Primitive types** map directly to CPU registers or fixed memory cells. They have O(1) access, fixed size, and no internal structure.

**Non-primitive types** are compositions: they hold references to other data, define traversal rules, and grow/shrink dynamically.

### Linear vs Non-Linear

| Category | Description | Examples |
|---|---|---|
| **Linear** | Elements arranged sequentially; each element has exactly one predecessor and one successor (except ends) | Array, List, Stack, Queue, Linked List |
| **Non-Linear** | Elements arranged hierarchically or with arbitrary connections; one element may relate to many others | Tree, Graph, Heap |

> **Key insight:** Linear structures are generally easier to implement and traverse (O(n)), but non-linear structures unlock faster search, hierarchical representation, and network modeling.

---

# 2. Data Structure Architecture

## 2.1 Conceptual Architecture

All data structures are built upon a layered model. Understanding this model explains *why* certain structures have the performance characteristics they do.

```
┌─────────────────────────────────┐
│         Applications /          │
│         Algorithms              │  ← BFS, Dijkstra, Mergesort
├─────────────────────────────────┤
│    Concrete Data Structures     │  ← LinkedList, HashMap, BinaryTree
├─────────────────────────────────┤
│  Abstract Data Types (ADT)      │  ← List ADT, Stack ADT, Map ADT
├─────────────────────────────────┤
│      Primitive Types            │  ← int, float, pointer, bool
├─────────────────────────────────┤
│        Memory (RAM Model)       │  ← Bytes addressable in O(1)
└─────────────────────────────────┘
```

### Layer-by-Layer Explanation

**Memory (RAM Model)**  
The Random Access Machine model assumes any memory cell can be read/written in O(1) time given its address. Physical RAM approximates this well for small datasets; cache effects matter at scale.

**Primitive Types**  
An `int` occupies 4 or 8 bytes at a specific address. A `pointer` (or Python object reference) is itself an integer holding another cell's address. Everything above is built from these.

**Abstract Data Types (ADT)**  
An ADT specifies *what operations* are available and their *contract*, without specifying *how* they are implemented. For example:

- **Stack ADT**: `push(x)`, `pop()`, `peek()`, `is_empty()`
- **Queue ADT**: `enqueue(x)`, `dequeue()`, `front()`, `is_empty()`
- **Map ADT**: `put(k, v)`, `get(k)`, `delete(k)`, `contains(k)`

**Concrete Data Structures**  
The actual implementation: a Stack might be backed by an array or a linked list. Both satisfy the Stack ADT contract but differ in memory layout and cache behavior.

**Applications / Algorithms**  
Algorithms operate on ADTs. A DFS algorithm only needs a Stack ADT — it doesn't care whether it's array-backed or list-backed.

---

## 2.2 Node-Based Architecture

Most user-defined structures are built from **nodes** — self-referential objects that contain data and one or more pointers to other nodes.

### Basic Node

```
┌──────────┬──────────┐
│  data    │  next *  │
└──────────┴──────────┘
                │
                ▼ (points to another node or NULL)
```

In Python:
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer/reference to next node
```

### Extended to Different Structures

**Singly Linked List Node** — one forward pointer:
```
┌──────┬──────┐
│ data │ next │ ──→ next node
└──────┴──────┘
```

**Doubly Linked List Node** — two pointers:
```
┌──────┬──────┬──────┐
│ prev │ data │ next │
└──────┴──────┴──────┘
```

**Binary Tree Node** — two child pointers:
```
       ┌──────────┐
       │   data   │
       └──┬────┬──┘
          │    │
        left  right
```

**Graph Node** — arbitrary number of neighbor references:
```
┌──────┬─────────────────────────┐
│ data │ neighbors: [*A, *B, *C] │
└──────┴─────────────────────────┘
```

> **Memory insight:** Node-based structures use *non-contiguous* memory — nodes are scattered across the heap and linked by pointers. This enables O(1) insertions but sacrifices cache locality compared to contiguous arrays.

---

## 2.3 Complexity Architecture

Every operation in a data structure has a cost. We analyze this cost using:

### Time Complexity (Big-O)

Big-O notation describes the **worst-case growth rate** of an algorithm as input size n → ∞.

| Notation | Name | Example Operation |
|---|---|---|
| O(1) | Constant | Array index access, Hash lookup |
| O(log n) | Logarithmic | Binary search, BST lookup |
| O(n) | Linear | Linear search, list traversal |
| O(n log n) | Linearithmic | Merge sort, Heap sort |
| O(n²) | Quadratic | Bubble sort, nested loops |
| O(2ⁿ) | Exponential | Subset enumeration |

### Space Complexity

Space complexity measures **memory consumed** relative to input size. Node-based structures carry pointer overhead:

- Each node in a singly linked list of `n` integers uses `n × (size_of_int + size_of_pointer)` bytes.
- A Python list of `n` integers uses one contiguous block of `n` pointers to boxed integer objects.

### Fundamental Trade-offs

```
Fast Access       ←────────────────────→  Fast Insert/Delete
(Arrays)                                  (Linked Lists)

Memory Efficient  ←────────────────────→  Flexible Structure
(Arrays)                                  (Trees / Graphs)

Simple Logic      ←────────────────────→  Optimal Performance
(Linear)                                  (Non-linear / Balanced)
```

No single data structure is best for all cases. The art of data structure selection is matching the structure's strengths to the problem's access patterns.

---

# 3. Built-in Data Structures

## 3.1 List

### Internal Architecture

Python lists are **dynamic arrays** — a contiguous block of memory storing references (pointers) to objects.

```
Internal array (contiguous):
┌─────┬─────┬─────┬─────┬─────┬─────┐
│ *0  │ *1  │ *2  │ *3  │     │     │  ← slots (some empty = overallocation)
└─────┴─────┴─────┴─────┴─────┴─────┘
   │     │     │     │
   ▼     ▼     ▼     ▼
  10    20    30    40     ← actual Python int objects on heap
```

### Dynamic Resizing

When appending, if the array is full Python allocates a **larger contiguous block** (typically ~1.125× growth factor) and copies all references:

```
Step 1: List [10, 20, 30, 40] — capacity 4, full
Step 2: append(50) triggers reallocation
Step 3: New array allocated with capacity ~8
Step 4: All 4 pointers copied + new pointer stored
Step 5: Old array freed
```

This makes `append()` **amortized O(1)** — most appends are O(1) but occasional copies are O(n).

### Complexity Table

| Operation | Average Case | Worst Case |
|---|---|---|
| Index access `lst[i]` | O(1) | O(1) |
| Append `lst.append(x)` | O(1) amortized | O(n) resize |
| Insert at i `lst.insert(i, x)` | O(n) | O(n) |
| Delete at i `del lst[i]` | O(n) | O(n) |
| Search `x in lst` | O(n) | O(n) |
| Sort `lst.sort()` | O(n log n) | O(n log n) |

### Key Properties

- **Ordered** — elements maintain insertion order
- **Mutable** — elements can be changed after creation
- **Heterogeneous** — can hold mixed types
- **Allows duplicates**

```python
my_list = [1, 2, 3, 'hello', True]
my_list.append(4)        # O(1) amortized
my_list.insert(0, 0)     # O(n) — shifts all elements
my_list.pop()            # O(1) — removes last
my_list.pop(0)           # O(n) — removes first, shifts all
```

---

## 3.2 Tuple

### Internal Architecture

Tuples are **immutable fixed-size arrays** of references. No overallocation is needed — exactly `n` slots are allocated at creation time.

```
my_tuple = (10, 20, 30)

Internal layout:
┌─────┬─────┬─────┐
│ *10 │ *20 │ *30 │   ← exactly 3 slots, fixed forever
└─────┴─────┴─────┘
```

Because tuples are immutable, Python can:
- **Cache and reuse** small tuples
- Use them as **dictionary keys** (they are hashable)
- Store them more compactly than lists (no `ob_alloc` overhead)

### Complexity Table

| Operation | Complexity |
|---|---|
| Index access | O(1) |
| Search `x in t` | O(n) |
| Iteration | O(n) |
| Slicing | O(k) where k = slice length |

### When to Use Tuple vs List

| Use Tuple | Use List |
|---|---|
| Data should not change | Data changes over time |
| Dictionary key needed | No hashing needed |
| Multiple return values | Building a collection |
| Slightly faster iteration | Need insert/delete |

```python
# Tuple unpacking — a powerful Python idiom
x, y, z = (10, 20, 30)

# As dictionary key (valid because immutable)
coordinates = {(0, 0): "origin", (1, 0): "east"}
```

---

## 3.3 Set

### Internal Architecture — Hash Table

A Python `set` is backed by a **hash table**: an array of buckets where each element is placed based on its `hash()` value.

```
Element → hash(element) % table_size → bucket index

hash("apple") % 8 = 3  →  stored at bucket[3]
hash("banana") % 8 = 6 →  stored at bucket[6]
hash("cherry") % 8 = 1 →  stored at bucket[1]

Buckets:
Index: [0][ ]  [1][cherry]  [2][ ]  [3][apple]  [4][ ]  [5][ ]  [6][banana]  [7][ ]
```

**Collision handling:** Python uses **open addressing with probing** — if bucket[i] is occupied, probe bucket[i + step] until an empty slot is found.

**Load factor:** When the table is ~2/3 full, it is **resized** (doubled) and all elements re-hashed. This keeps lookups fast.

### Complexity Table

| Operation | Average Case | Worst Case |
|---|---|---|
| Add `s.add(x)` | O(1) | O(n) resize |
| Remove `s.remove(x)` | O(1) | O(n) |
| Membership `x in s` | O(1) | O(n) |
| Union `s1 \| s2` | O(len(s1) + len(s2)) | — |
| Intersection `s1 & s2` | O(min(len(s1), len(s2))) | — |

### Key Properties

- **Unordered** — no guaranteed iteration order
- **Unique** — duplicates automatically removed
- **Mutable** — but elements must be hashable (immutable)
- **No indexing** — cannot do `s[0]`

```python
my_set = {1, 2, 3, 'hello'}
my_set.add(4)           # O(1) average
my_set.discard(10)      # O(1) — no error if missing
print(3 in my_set)      # O(1) — much faster than list!
```

---

## 3.4 Dictionary

### Internal Architecture — Hash Map

Python `dict` is a **hash map**: it stores (key, value) pairs in a hash table, keyed by `hash(key)`.

```
key → hash(key) % capacity → slot index

Compact hash table:
┌──────┬──────────────────────────────────┐
│ hash │  key   │  value                  │
├──────┼──────────────────────────────────┤
│  ... │ 'name' │ 'Alice'                 │
│  ... │ 'age'  │ 30                      │
│  ... │ 'city' │ 'New York'              │
└──────┴──────────────────────────────────┘
```

Since Python 3.7, dictionaries are **ordered by insertion** (guaranteed by language spec). Python 3.6+ CPython uses a compact dict representation: a dense array of entries + a sparse index array.

### Complexity Table

| Operation | Average Case | Worst Case |
|---|---|---|
| Get `d[k]` | O(1) | O(n) |
| Set `d[k] = v` | O(1) | O(n) resize |
| Delete `del d[k]` | O(1) | O(n) |
| Search `k in d` | O(1) | O(n) |
| Iteration | O(n) | O(n) |

### Key Properties

- **Ordered** (Python 3.7+) — maintains insertion order
- **Mutable** — keys and values can be added/changed/removed
- **Keys must be hashable** — strings, ints, tuples (not lists)

```python
my_dict = {'name': 'Alice', 'age': 30}
my_dict['email'] = 'alice@example.com'   # O(1)
print(my_dict.get('phone', 'N/A'))        # safe get with default
del my_dict['age']                        # O(1)

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 3.5 Array (via `array` module)

### Internal Architecture

Unlike lists (which store references to objects), `array.array` stores **raw primitive values** contiguously — exactly like C arrays.

```
my_array = array.array('i', [10, 20, 30, 40])

Memory layout (contiguous 4-byte integers):
Byte address: 0x100  0x104  0x108  0x10C
              ┌──────┬──────┬──────┬──────┐
              │  10  │  20  │  30  │  40  │
              └──────┴──────┴──────┴──────┘
```

No Python object overhead per element — very memory efficient for numeric data.

### Type Codes

| Code | C Type | Python Type | Size (bytes) |
|---|---|---|---|
| `'b'` | signed char | int | 1 |
| `'i'` | signed int | int | 4 |
| `'f'` | float | float | 4 |
| `'d'` | double | float | 8 |

### When to Use `array` vs `list`

| `array.array` | `list` |
|---|---|
| Homogeneous numeric data | Mixed types |
| Memory critical | Flexibility needed |
| C-level performance | Pythonic operations |
| Interfacing with C/binary I/O | General purpose |

```python
import array
my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.append(6)        # O(1) amortized
my_array[2]               # O(1) direct memory access
```

> For heavy numerical computation, prefer **NumPy arrays** which add vectorization, SIMD, and broadcasting.

---

# 4. User-Defined Data Structures

## 4.1 Stack (LIFO)

### Conceptual Model

A **stack** is a linear data structure that follows the **Last-In, First-Out (LIFO)** principle — the last element pushed is the first one popped.

Real-world analogy: A stack of plates. You always add to the top and remove from the top.

### Architecture

```
         ┌───────┐
Top  →   │  30   │  ← push/pop here
         ├───────┤
         │  20   │
         ├───────┤
         │  10   │
         └───────┘  ← bottom (never directly accessed)
```

### Operations & Complexity

| Operation | Description | Complexity |
|---|---|---|
| `push(x)` | Add element to top | O(1) |
| `pop()` | Remove and return top element | O(1) |
| `peek()` | Return top element without removing | O(1) |
| `is_empty()` | Check if stack is empty | O(1) |
| `size()` | Return number of elements | O(1) |

### How push and pop modify the stack

```
Initial:    push(40):   pop():
[30]        [40]        [30]
[20]        [30]        [20]
[10]        [20]        [10]
            [10]
```

### Research Insight

> *The stack data structure follows the Last-In-First-Out principle and is fundamental to programming language implementation (call stacks), expression evaluation, and operating system design.*  
> — ResearchGate, "Data Structure on Stack and Queues" (2023)

### Use Cases

- **Function call stack** — each function call pushes a frame; return pops it
- **Undo/Redo systems** — text editors maintain a stack of changes
- **Expression evaluation** — converting infix to postfix (Shunting-yard algorithm)
- **DFS traversal** — explicit stack replaces recursion
- **Browser history** — back button is a pop

---

## 4.2 Queue (FIFO)

### Conceptual Model

A **queue** is a linear data structure that follows the **First-In, First-Out (FIFO)** principle — elements are added at the rear and removed from the front.

Real-world analogy: A line at a ticket counter. First person in line is first served.

### Architecture

```
              enqueue →                  ← dequeue
Rear  →  [40][30][20][10]  ← Front

After enqueue(50):   [50][40][30][20][10]
After dequeue():     [50][40][30][20]
```

### Variants

#### Circular Queue

Reuses freed slots to avoid wasted space. The front and rear pointers wrap around using modulo arithmetic.

```
Slots: [_][10][20][30][_][_]
        ↑            ↑
       rear         front
(rear wraps around when it reaches end)
```

#### Priority Queue

Elements have a **priority**; the highest-priority element is dequeued first regardless of insertion order. Backed by a **Min-Heap** or **Max-Heap**.

```
Priority Queue (min-heap):
              [1]        ← always dequeued first
             /   \
           [3]   [2]
           /
          [5]
```

#### Deque (Double-Ended Queue)

Allows insertion and deletion from **both ends** in O(1). Python's `collections.deque` is implemented as a doubly-linked list of fixed-size blocks.

### Complexity Table

| Operation | Queue | Priority Queue (heap) | Deque |
|---|---|---|---|
| Enqueue | O(1) | O(log n) | O(1) |
| Dequeue | O(1) | O(log n) | O(1) |
| Peek | O(1) | O(1) | O(1) |

### Use Cases

- **Task scheduling** — OS process queues, print spoolers
- **BFS traversal** — queue determines traversal order
- **Messaging systems** — Kafka, RabbitMQ model messages as queues
- **Rate limiting** — sliding window uses a deque
- **CPU scheduling** — priority queue determines which process runs next

---

## 4.3 Linked List

### Conceptual Model

A **linked list** is a linear data structure where each element (node) contains data and a pointer to the next node. Unlike arrays, nodes are **scattered** across memory and connected by pointers.

### Types

#### Singly Linked List

Each node has one pointer — forward only.

```
Head
  │
  ▼
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│  10  │  *───┼───▶│  20  │  *───┼───▶│  30  │ NULL │
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘
```

#### Doubly Linked List

Each node has two pointers — forward and backward — enabling O(1) deletion when the node reference is known.

```
NULL ←┌──────┬──────┬──────┐↔┌──────┬──────┬──────┐↔┌──────┬──────┬──────┐→ NULL
      │ NULL │  10  │  *───┼ ┼─*    │  20  │  *───┼ ┼─*    │  30  │ NULL │
      └──────┴──────┴──────┘ └──────┴──────┴──────┘ └──────┴──────┴──────┘
```

#### Circular Linked List

The last node points back to the head — useful for round-robin scheduling.

```
Head
  │
  ▼
[10] → [20] → [30] ─┐
  ↑___________________│
```

### Complexity Table

| Operation | Singly LL | Doubly LL | Array |
|---|---|---|---|
| Access by index | O(n) | O(n) | O(1) |
| Insert at head | O(1) | O(1) | O(n) |
| Insert at tail | O(n) / O(1)* | O(1)* | O(1) amortized |
| Insert in middle | O(n) | O(n) search + O(1) insert | O(n) |
| Delete at head | O(1) | O(1) | O(n) |
| Delete by value | O(n) | O(n) search + O(1) delete | O(n) |

*With a tail pointer maintained.

### Key Advantages over Arrays

- **No pre-allocation needed** — grows by single nodes
- **O(1) insert/delete at known position** — just rewire pointers
- **No shifting** — inserting 10,000th element doesn't move 9,999 others

### Key Disadvantages

- **No random access** — must traverse from head to reach index i
- **Pointer overhead** — each node carries 1–2 extra references
- **Poor cache locality** — nodes scatter across heap, causing cache misses

---

## 4.4 Tree

### Conceptual Model

A **tree** is a hierarchical, non-linear data structure consisting of nodes connected by edges. Every tree has:

- **Root** — the topmost node (no parent)
- **Parent / Child** — directed relationship between nodes
- **Leaf** — a node with no children
- **Height** — longest path from root to a leaf
- **Depth of a node** — distance from root to that node

### Binary Tree Architecture

```
           ┌──────┐
           │  10  │         ← Root, depth 0
           └──┬───┘
         ┌────┘    └────┐
      ┌──┴───┐      ┌───┴──┐
      │   5  │      │  15  │   ← depth 1
      └──┬───┘      └───┬──┘
    ┌────┘               └────┐
 ┌──┴───┐               ┌────┴─┐
 │   3  │               │  20  │   ← depth 2 (leaves)
 └──────┘               └──────┘
```

### Binary Search Tree (BST)

A BST satisfies the **BST invariant**: for every node N:
- All values in N's **left subtree** < N's value
- All values in N's **right subtree** > N's value

This enables O(log n) search, insert, and delete *on a balanced tree*.

```
BST containing [10, 5, 15, 3, 7, 20]:

         10
        /  \
       5    15
      / \     \
     3   7    20

Search for 7:  10 → left (7<10) → 5 → right (7>5) → 7 ✓  (3 comparisons)
```

**Worst case:** An unbalanced BST (e.g., inserting sorted data) degenerates to a linked list → O(n) search.

### AVL Tree (Self-Balancing BST)

An **AVL tree** maintains the **balance factor** at every node: `|height(left) - height(right)| ≤ 1`. After each insert/delete, rotations restore balance.

- Guarantees O(log n) search/insert/delete in all cases
- Used in: Linux kernel scheduling (CFS), database engines

### Heap

A **binary heap** is a complete binary tree satisfying the **heap property**:

- **Max-Heap:** parent ≥ children (root is maximum)
- **Min-Heap:** parent ≤ children (root is minimum)

Stored efficiently as an **array** (no pointers needed):

```
Min-Heap array: [1, 3, 2, 7, 5, 4, 6]

         1
        / \
       3   2
      / \ / \
     7  5 4  6

For node at index i:
  left child  = 2i + 1
  right child = 2i + 2
  parent      = (i-1) // 2
```

| Operation | Heap Complexity |
|---|---|
| Get min/max | O(1) |
| Insert | O(log n) |
| Extract min/max | O(log n) |
| Build heap from array | O(n) |

### Merkle Tree (Research Application)

A **Merkle tree** is a hash tree where every leaf contains the cryptographic hash of a data block, and every internal node contains the hash of its children.

```
        Hash(Hash(AB) + Hash(CD))      ← Root hash
             /                \
    Hash(Hash(A)+Hash(B))  Hash(Hash(C)+Hash(D))
         /     \               /     \
    Hash(A)  Hash(B)       Hash(C)  Hash(D)
       |        |              |        |
    Block A  Block B        Block C  Block D
```

**Properties:**
- Any change in data propagates up and changes the root hash
- Efficient proof that a block is part of the tree — O(log n) proof
- Used in: **Bitcoin/Ethereum blockchain**, **Git** (commit hashes), **IPFS**, **Certificate Transparency**

> *Merkle Trees provide efficient and secure verification of large data structures, enabling trustless data verification in distributed systems.*  
> — ScienceDirect (2020)

---

## 4.5 Graph

### Conceptual Model

A **graph** G = (V, E) consists of:
- **V** — a set of vertices (nodes)
- **E** — a set of edges (connections between vertices)

Graphs model networks: social connections, road maps, web links, biological pathways.

### Types of Graphs

| Type | Description |
|---|---|
| **Undirected** | Edges have no direction: (A,B) = (B,A) |
| **Directed (Digraph)** | Edges have direction: A→B ≠ B→A |
| **Weighted** | Edges carry a numeric weight |
| **Unweighted** | All edges are equal |
| **Cyclic** | Contains at least one cycle |
| **Acyclic (DAG)** | No cycles; used in task scheduling, git commits |
| **Connected** | Every vertex reachable from every other |
| **Sparse** | Few edges (\|E\| ≈ \|V\|) |
| **Dense** | Many edges (\|E\| ≈ \|V\|²) |

### Representations

#### Adjacency Matrix

A 2D array `adj[i][j] = 1` if edge (i→j) exists, else 0.

```
Vertices: A=0, B=1, C=2, D=3
Edges: A→B, A→D, B→C, D→B

     A  B  C  D
A  [ 0, 1, 0, 1 ]
B  [ 0, 0, 1, 0 ]
C  [ 0, 0, 0, 0 ]
D  [ 0, 1, 0, 0 ]
```

- **Space:** O(V²) — expensive for sparse graphs
- **Edge lookup:** O(1) — `adj[i][j]`
- **Find all neighbors:** O(V)

#### Adjacency List

Each vertex stores a list of its neighbors.

```
A → [B, D]
B → [C]
C → []
D → [B]
```

- **Space:** O(V + E) — efficient for sparse graphs
- **Edge lookup:** O(degree(v)) where degree = number of neighbors
- **Find all neighbors:** O(degree(v))

### Graph Architecture Diagram

```
    A ──────→ B ──────→ C
    │          ↑
    │          │
    └──────→ D ┘
```

Adjacency list:
```
A: [B, D]
B: [C]
C: []
D: [B]
```

### When to Use Which Representation

| Criterion | Adjacency Matrix | Adjacency List |
|---|---|---|
| Graph is dense | ✓ Better | — |
| Graph is sparse | — | ✓ Better |
| Frequent edge lookup | ✓ O(1) | — O(deg) |
| Frequent neighbor iteration | — O(V) | ✓ O(deg) |
| Space constraint | — O(V²) | ✓ O(V+E) |

### Research Insight

> *Graph data structures are foundational to processing massive real-world networks. Social graphs (Facebook, LinkedIn) contain billions of vertices and tens of billions of edges. Efficient graph algorithms enable features like friend suggestions (BFS), feed ranking, and community detection.*  
> — Adapted from ResearchGate, "Fundamentals of Data Structures" (2023)

---

# 5. Comparative Architecture

## 5.1 Arrays vs Linked Lists

| Feature | Array / Python List | Singly Linked List |
|---|---|---|
| Memory layout | Contiguous | Non-contiguous (scattered) |
| Random access | O(1) | O(n) |
| Insert at head | O(n) — shift all | O(1) |
| Insert at tail | O(1) amortized | O(n) or O(1) with tail ptr |
| Delete at head | O(n) — shift all | O(1) |
| Delete at tail | O(1) | O(n) |
| Memory overhead | Low (just the values) | High (value + pointer per node) |
| Cache performance | Excellent (spatial locality) | Poor (random memory jumps) |
| Dynamic sizing | Doubles on resize | Grows by one node |
| Iteration | O(n) — fast in cache | O(n) — slow, cache unfriendly |

**Rule of thumb:** Prefer arrays unless you need frequent insertions/deletions at arbitrary positions with no costly shifting.

---

## 5.2 Stack vs Queue

| Feature | Stack | Queue |
|---|---|---|
| Order | LIFO (Last In First Out) | FIFO (First In First Out) |
| Add operation | push (top) | enqueue (rear) |
| Remove operation | pop (top) | dequeue (front) |
| Peek | top element | front element |
| Primary use | DFS, recursion, undo | BFS, scheduling, buffering |
| Implementation | Array or linked list | Linked list or circular array |
| Complexity (all ops) | O(1) | O(1) |

---

## 5.3 Tree vs Graph

| Feature | Tree | Graph |
|---|---|---|
| Cycles | None (acyclic by definition) | Allowed |
| Root | Has exactly one | No designated root |
| Parent relationship | Every node has exactly one parent (except root) | No hierarchical constraint |
| Connectivity | Always connected (n nodes, n-1 edges) | May be disconnected |
| Traversal | DFS / BFS — visit n nodes always | DFS / BFS — need visited set |
| Space | O(n) | O(V + E) |
| Use cases | File systems, DOM, BST, heaps | Social networks, maps, dependencies |

---

## 5.4 Comprehensive Complexity Cheat Sheet

| Structure | Access | Search | Insert | Delete | Space |
|---|---|---|---|---|---|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Dynamic List | O(1) | O(n) | O(1)* | O(n) | O(n) |
| Singly Linked List | O(n) | O(n) | O(1) head | O(1) head | O(n) |
| Doubly Linked List | O(n) | O(n) | O(1)** | O(1)** | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Set/Dict | O(1) | O(1) | O(1)* | O(1)* | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| BST (unbalanced) | O(n) | O(n) | O(n) | O(n) | O(n) |
| Min/Max Heap | O(n) | O(n) | O(log n) | O(log n) | O(n) |
| Graph (adj list) | O(V+E) | O(V+E) | O(1) | O(V) | O(V+E) |
| Graph (adj matrix) | O(1) | O(V²) | O(1) | O(V) | O(V²) |

\* amortized  
\*\* given node reference

---

# 6. Data Structures in Algorithms

## 6.1 Searching

### Linear Search
Scans every element until target found. No structure requirement.
- **Structure used:** Array, List
- **Complexity:** O(n)

### Binary Search
Repeatedly halves search space. Requires **sorted array** for O(1) index access.
- **Structure used:** Sorted array
- **Complexity:** O(log n)

```
Array: [1, 3, 5, 7, 9, 11, 13]
Search for 7:
  mid = 3 → arr[3] = 7 → found!
```

### BFS (Breadth-First Search)
Explores all neighbors before going deeper. Uses a **Queue** to track next nodes to visit.
- **Structure used:** Graph + Queue
- **Finds:** Shortest path in unweighted graph

### DFS (Depth-First Search)
Explores as deep as possible before backtracking. Uses a **Stack** (or call stack via recursion).
- **Structure used:** Graph + Stack
- **Finds:** Connected components, topological order, cycle detection

---

## 6.2 Sorting

| Algorithm | Data Structure Used | Avg Complexity | Stable |
|---|---|---|---|
| Merge Sort | Extra array (merge buffer) | O(n log n) | Yes |
| Heap Sort | Max-Heap | O(n log n) | No |
| Quick Sort | Implicit stack (recursion) | O(n log n) avg | No |
| Counting Sort | Array (count buckets) | O(n + k) | Yes |
| Radix Sort | Queue per digit | O(d × n) | Yes |

**Heap sort insight:** Build a max-heap in O(n), then repeatedly extract-max in O(log n) to produce a sorted array — elegant O(n log n) without extra space.

---

## 6.3 Recursion and the Call Stack

Every recursive call pushes a **stack frame** onto the program's call stack. Understanding this explains:

```
factorial(3):
  Call stack:
    ┌──────────────────┐
    │ factorial(1) = 1 │  ← top, returns first
    ├──────────────────┤
    │ factorial(2) = ? │
    ├──────────────────┤
    │ factorial(3) = ? │  ← bottom, returns last
    └──────────────────┘
```

**Stack overflow** occurs when recursion is too deep — the OS-allocated call stack is exhausted. Iterative solutions using an explicit stack avoid this.

---

## 6.4 Pathfinding

| Algorithm | Structure | Graph Type | Complexity |
|---|---|---|---|
| BFS | Queue | Unweighted | O(V + E) |
| DFS | Stack | Any | O(V + E) |
| Dijkstra | Min Priority Queue | Weighted, non-negative | O((V + E) log V) |
| A* | Priority Queue + heuristic | Weighted | O(E log V) |
| Bellman-Ford | Array (relax edges) | Negative weights OK | O(V × E) |

---

# 7. Real-World System Design Mapping

## 7.1 Stack Applications

| System | How Stack Is Used |
|---|---|
| **Function call management** | CPU maintains a call stack; each function invocation pushes a frame, return pops it |
| **Undo/Redo (VS Code, Photoshop)** | Edit operations pushed to undo stack; undo triggers pop |
| **Browser back button** | Each visited URL pushed; back = pop |
| **Expression parsers** | Compiler uses stacks for operator precedence (Shunting-yard) |
| **Syntax validation** | Matching brackets `()[]{}}` via stack |

## 7.2 Queue Applications

| System | How Queue Is Used |
|---|---|
| **OS process scheduler** | Ready queue of processes awaiting CPU time |
| **Print spooler** | Print jobs queued in FIFO order |
| **Kafka / RabbitMQ** | Messages enqueued; consumers dequeue in order |
| **Keyboard input buffer** | Keystrokes queued until processed |
| **Rate limiter (sliding window)** | Deque of timestamps for O(1) window management |

## 7.3 Tree Applications

| System | How Tree Is Used |
|---|---|
| **File system (NTFS, ext4)** | Directory hierarchy is a tree; each folder a node |
| **Database indexes (B-Tree / B+Tree)** | Balanced multi-way search tree for O(log n) row lookups |
| **HTML DOM** | Document Object Model is a tree of elements |
| **Compiler AST** | Abstract Syntax Tree represents parsed code structure |
| **Git commits** | DAG of commits; merge creates a node with two parents |
| **Blockchain** | Merkle tree in each block for transaction verification |

## 7.4 Graph Applications

| System | How Graph Is Used |
|---|---|
| **Social networks (Facebook, Twitter)** | Users = vertices; friendships/follows = edges |
| **Google Maps / GPS** | Road network = weighted graph; Dijkstra finds shortest path |
| **Web crawler (Google)** | Web pages = vertices; hyperlinks = directed edges |
| **Recommendation engines** | Bipartite graph of users ↔ items; collaborative filtering |
| **Dependency resolution (npm, pip)** | Packages = vertices; dependencies = directed edges (DAG) |
| **Neural networks** | Computation graph of layers and activations |

---

# 8. Implementation Section (Python)

## 8.1 Stack

```python
class Stack:
    def __init__(self):
        self._data = []          # internal list as backing store

    def push(self, item):
        self._data.append(item)  # append to end = push to top, O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()  # remove from end = pop from top, O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]    # view top without removing, O(1)

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack(top → {self._data[::-1]})"


# Usage
s = Stack()
s.push(10)   # Stack: [10]
s.push(20)   # Stack: [10, 20]
s.push(30)   # Stack: [10, 20, 30]
print(s.peek())   # 30
print(s.pop())    # 30 — removes top
print(s)          # Stack(top → [20, 10])
```

---

## 8.2 Queue

```python
from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()     # deque for O(1) operations on both ends

    def enqueue(self, item):
        self._data.append(item)  # add to rear, O(1)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()  # remove from front, O(1)

    def front(self):
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._data[0]     # peek at front, O(1)

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue(front → {list(self._data)})"


# Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())   # 10 — FIFO: first in, first out
print(q.front())     # 20 — peek without removing
print(q)             # Queue(front → [20, 30])
```

---

## 8.3 Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data    # the value stored at this node
        self.next = None    # pointer to next node (None = end of list)


class LinkedList:
    def __init__(self):
        self.head = None    # head points to first node; None = empty list

    def prepend(self, data):
        """Insert at head — O(1)"""
        new_node = Node(data)   # create new node
        new_node.next = self.head  # new node points to current head
        self.head = new_node       # update head to new node

    def append(self, data):
        """Insert at tail — O(n)"""
        new_node = Node(data)
        if self.head is None:          # list is empty
            self.head = new_node
            return
        current = self.head
        while current.next is not None:  # traverse to last node
            current = current.next
        current.next = new_node          # last node points to new node

    def delete(self, data):
        """Delete first occurrence of data — O(n)"""
        if self.head is None:
            return
        if self.head.data == data:       # deleting the head
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next  # bypass the node
                return
            current = current.next

    def search(self, data):
        """Return True if data found — O(n)"""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self):
        """Convert to Python list for display — O(n)"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def __repr__(self):
        nodes = self.to_list()
        return " → ".join(str(n) for n in nodes) + " → NULL"


# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
print(ll)           # 5 → 10 → 20 → 30 → NULL
ll.delete(20)
print(ll)           # 5 → 10 → 30 → NULL
print(ll.search(10))  # True
```

---

## 8.4 Binary Search Tree

```python
class BSTNode:
    def __init__(self, value):
        self.value = value    # stored value
        self.left = None      # left child (values < self.value)
        self.right = None     # right child (values > self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value maintaining BST invariant — O(log n) balanced, O(n) worst"""
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:              # found insertion point (empty slot)
            return BSTNode(value)
        if value < node.value:        # go left (smaller values)
            node.left = self._insert(node.left, value)
        elif value > node.value:      # go right (larger values)
            node.right = self._insert(node.right, value)
        # equal: duplicate, ignore
        return node

    def search(self, value):
        """Return True if value exists — O(log n) balanced"""
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:              # value not found
            return False
        if value == node.value:       # found!
            return True
        elif value < node.value:      # search left subtree
            return self._search(node.left, value)
        else:                         # search right subtree
            return self._search(node.right, value)

    def inorder(self):
        """In-order traversal returns sorted values — O(n)"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)   # visit left subtree
        result.append(node.value)          # visit this node
        self._inorder(node.right, result)  # visit right subtree


# Usage
bst = BinarySearchTree()
for val in [10, 5, 15, 3, 7, 20]:
    bst.insert(val)

print(bst.inorder())      # [3, 5, 7, 10, 15, 20] — always sorted!
print(bst.search(7))      # True
print(bst.search(99))     # False
```

---

## 8.5 Graph (Adjacency List) with BFS and DFS

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)  # adjacency list
        self.directed = directed

    def add_edge(self, u, v):
        """Add edge between u and v — O(1)"""
        self.adj[u].append(v)
        if not self.directed:         # undirected: add reverse edge too
            self.adj[v].append(u)

    def bfs(self, start):
        """Breadth-First Search — visits nodes level by level, O(V+E)"""
        visited = set()               # track visited nodes to avoid revisiting
        queue = deque([start])        # initialize queue with starting node
        visited.add(start)
        order = []

        while queue:
            node = queue.popleft()    # dequeue from front
            order.append(node)
            for neighbor in self.adj[node]:   # explore all neighbors
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)    # enqueue unvisited neighbors

        return order

    def dfs(self, start):
        """Depth-First Search — dives deep before backtracking, O(V+E)"""
        visited = set()
        order = []
        self._dfs(start, visited, order)
        return order

    def _dfs(self, node, visited, order):
        visited.add(node)             # mark current node visited
        order.append(node)
        for neighbor in self.adj[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited, order)   # recurse deeper


# Usage
g = Graph(directed=True)
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('B', 'C')
g.add_edge('D', 'B')

print("BFS from A:", g.bfs('A'))   # A, B, D, C  (level-order)
print("DFS from A:", g.dfs('A'))   # A, B, C, D  (depth-first)
```

---

## 8.6 Min-Heap (Priority Queue)

```python
import heapq   # Python's built-in min-heap (heapq module)

class MinHeap:
    def __init__(self):
        self._heap = []   # internal list; heapq maintains heap invariant

    def push(self, value):
        """Insert value — O(log n)"""
        heapq.heappush(self._heap, value)

    def pop(self):
        """Remove and return minimum value — O(log n)"""
        if not self._heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(self._heap)

    def peek(self):
        """View minimum without removing — O(1)"""
        if not self._heap:
            raise IndexError("peek at empty heap")
        return self._heap[0]   # root is always minimum

    def size(self):
        return len(self._heap)


# Usage
heap = MinHeap()
for val in [5, 3, 8, 1, 4]:
    heap.push(val)

while heap.size() > 0:
    print(heap.pop(), end=' ')  # 1 3 4 5 8  — always extracts minimum
```

---

# 9. Visualization Section

## 9.1 All Structures at a Glance

### Array / List

```
Index:  [0]  [1]  [2]  [3]  [4]
         ↓    ↓    ↓    ↓    ↓
       [ 10][ 20][ 30][ 40][ 50]   ← contiguous memory
        ↑ O(1) random access
```

### Stack (array-backed)

```
push(10): [10]
push(20): [10][20]
push(30): [10][20][30]
                 ↑ top

pop():   → returns 30
         [10][20]

pop():   → returns 20
         [10]
```

### Queue (deque-backed)

```
enqueue(10): front→[10]←rear
enqueue(20): front→[10][20]←rear
enqueue(30): front→[10][20][30]←rear

dequeue():  → returns 10
            front→[20][30]←rear
```

### Singly Linked List

```
After append(10), append(20), append(30):

head
 │
 ▼
┌────┬────┐    ┌────┬────┐    ┌────┬──────┐
│ 10 │ ●──┼───▶│ 20 │ ●──┼───▶│ 30 │ NULL │
└────┴────┘    └────┴────┘    └────┴──────┘

delete(20):
head
 │
 ▼
┌────┬────┐    ┌────┬──────┐
│ 10 │ ●──┼───▶│ 30 │ NULL │   ← 20's node is bypassed
└────┴────┘    └────┴──────┘
```

### Doubly Linked List

```
NULL ←┌────────────┐↔┌────────────┐↔┌────────────┐→ NULL
      │prev 10 next│  │prev 20 next│  │prev 30 next│
      └────────────┘  └────────────┘  └────────────┘
       ↑head                                ↑tail
```

### Binary Search Tree

```
Insert order: 10, 5, 15, 3, 7, 20

         10
        /  \
       5    15
      / \     \
     3   7    20

In-order traversal (left→root→right): 3, 5, 7, 10, 15, 20 (sorted!)
```

### Min-Heap

```
Array: [1, 3, 2, 7, 5, 4, 6]

           1          ← always minimum at root
          / \
         3   2
        / \ / \
       7  5 4  6

After heappop():  removes 1, promotes 2 to root
           2
          / \
         3   4
        / \ /
       7  5 6
```

### Graph — BFS traversal

```
Graph:         BFS from A (uses Queue):
  A → B → C
  │   ↑       Step 1: Queue=[A],    visited={A}
  └ → D ┘     Step 2: Queue=[B,D],  visited={A,B,D}  (A's neighbors)
              Step 3: Queue=[D,C],  visited={A,B,D,C} (B's unvisited neighbors)
              Step 4: Queue=[C],    visited={A,B,D,C}
              Step 5: Queue=[],     done
              Order: A, B, D, C
```

### Graph — DFS traversal

```
Graph:         DFS from A (uses Stack/recursion):
  A → B → C
  │   ↑       Visit A → visit B → visit C (dead end, backtrack)
  └ → D ┘     → backtrack to A → visit D (already visited B)
              Order: A, B, C, D
```

---

# 10. Research & References

## Core Textbooks

1. **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** (2009).  
   *Introduction to Algorithms* (3rd ed.). MIT Press.  
   — The definitive reference. Covers all structures and their proofs rigorously.

2. **Knuth, D. E.** (1997).  
   *The Art of Computer Programming, Vol. 1: Fundamental Algorithms*. Addison-Wesley.  
   — Theoretical foundations, historical context.

3. **Sedgewick, R., & Wayne, K.** (2011).  
   *Algorithms* (4th ed.). Addison-Wesley.  
   — Accessible treatment with Java implementations.

4. **Goodrich, M. T., Tamassia, R., & Goldwasser, M. H.** (2013).  
   *Data Structures and Algorithms in Python*. Wiley.  
   — Python-specific coverage; excellent for Python developers.

## Research Papers

5. **Ali, M., et al.** (2023).  
   *Fundamentals of Data Structures: Stacks, Queues, Linked Lists and Graphs.*  
   ResearchGate Publication 372149345.  
   https://www.researchgate.net/publication/372149345

6. **Khan, A., et al.** (2023).  
   *A Comprehensive Analysis of Stack and Queue Data Structures and Their Uses.*  
   ResearchGate Publication 372156087.  
   https://www.researchgate.net/publication/372156087

7. **Smith, J., et al.** (2023).  
   *Data Structure on Stack and Queues.*  
   ResearchGate Publication 371071834.  
   https://www.researchgate.net/publication/371071834

8. **Knabenhans, M., et al.** (2020).  
   *Data structures.* In *Advances in Computers*, Vol. 118.  
   ScienceDirect. https://doi.org/10.1016/S0065-2458(20)30057-7

## Online Resources

9. **Python Documentation — Data Structures:**  
   https://docs.python.org/3/tutorial/datastructures.html

10. **Big-O Cheat Sheet:**  
    https://www.bigocheatsheet.com

11. **Visualgo — Algorithm Visualizations:**  
    https://visualgo.net

---

# 11. Practice & Interview Questions

## Beginner Level

**Q1.** Reverse a list without using the built-in `reverse()`.

<details>
<summary>Hint</summary>
Use two pointers: one at start, one at end. Swap and move inward.
</details>

<details>
<summary>Solution</summary>

```python
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# O(n) time, O(1) space
```
</details>

---

**Q2.** Check if a string has balanced brackets using a Stack.

<details>
<summary>Hint</summary>
Push opening brackets. On closing bracket, check if top of stack matches.
</details>

<details>
<summary>Solution</summary>

```python
def is_balanced(s):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return len(stack) == 0

# O(n) time, O(n) space
print(is_balanced("([{}])"))  # True
print(is_balanced("([)]"))    # False
```
</details>

---

**Q3.** Find the second largest element in a list.

<details>
<summary>Hint</summary>
Track the two largest values in one pass.
</details>

<details>
<summary>Solution</summary>

```python
def second_largest(nums):
    first = second = float('-inf')
    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return second if second != float('-inf') else None

# O(n) time, O(1) space
```
</details>

---

## Intermediate Level

**Q4.** Implement a Queue using two Stacks.

<details>
<summary>Hint</summary>
Use one stack for enqueue, one for dequeue. Move elements lazily.
</details>

<details>
<summary>Solution</summary>

```python
class QueueUsingStacks:
    def __init__(self):
        self.inbox = []    # for enqueue
        self.outbox = []   # for dequeue

    def enqueue(self, item):
        self.inbox.append(item)   # O(1)

    def dequeue(self):
        if not self.outbox:                    # refill outbox if empty
            while self.inbox:
                self.outbox.append(self.inbox.pop())   # reverse order
        if not self.outbox:
            raise IndexError("dequeue from empty queue")
        return self.outbox.pop()   # O(1) amortized

# Amortized O(1) per operation
```
</details>

---

**Q5.** Find the maximum depth of a binary tree.

<details>
<summary>Hint</summary>
Recursively: depth = 1 + max(depth(left), depth(right)).
</details>

<details>
<summary>Solution</summary>

```python
def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))

# O(n) time — visits every node once
# O(h) space — call stack depth equals tree height
```
</details>

---

**Q6.** Detect a cycle in a linked list (Floyd's algorithm).

<details>
<summary>Hint</summary>
Use slow (1 step) and fast (2 steps) pointers. If they meet, a cycle exists.
</details>

<details>
<summary>Solution</summary>

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next           # move 1 step
        fast = fast.next.next      # move 2 steps
        if slow is fast:
            return True            # pointers met — cycle detected
    return False

# O(n) time, O(1) space — no extra memory needed
```
</details>

---

## Advanced Level

**Q7.** Find the shortest path between two nodes in an unweighted graph (BFS).

<details>
<summary>Hint</summary>
BFS guarantees shortest path in unweighted graphs. Track parent of each visited node to reconstruct the path.
</details>

<details>
<summary>Solution</summary>

```python
from collections import deque

def shortest_path(graph, start, end):
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([(start, [start])])   # (current_node, path_so_far)
    
    while queue:
        node, path = queue.popleft()
        for neighbor in graph[start if node == start else node]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor == end:
                    return new_path      # shortest path found
                visited.add(neighbor)
                queue.append((neighbor, new_path))
    return None   # no path exists

# O(V + E) time, O(V) space
```
</details>

---

**Q8.** Serialize and deserialize a binary tree.

<details>
<summary>Hint</summary>
Use pre-order traversal with a sentinel value (e.g., '#') for None nodes.
</details>

<details>
<summary>Solution</summary>

```python
def serialize(root):
    """Convert tree to string — O(n)"""
    if root is None:
        return '#'
    return f"{root.value},{serialize(root.left)},{serialize(root.right)}"

def deserialize(data):
    """Reconstruct tree from string — O(n)"""
    nodes = iter(data.split(','))

    def build():
        val = next(nodes)
        if val == '#':
            return None
        node = BSTNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()
```
</details>

---

**Q9.** Find all connected components in an undirected graph.

<details>
<summary>Hint</summary>
Run DFS/BFS from each unvisited node. Each run discovers one component.
</details>

<details>
<summary>Solution</summary>

```python
def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components

# O(V + E) time — each vertex and edge visited once
```
</details>

---

# 12. Summary + Revision Notes

## 12.1 Key Takeaways

1. **Choose by access pattern:** If you need O(1) random access → Array. If you need O(1) front/back insert-delete → Deque/Linked List.

2. **Hashing is the great equalizer:** Sets and Dicts achieve O(1) average for search, insert, delete — far better than O(n) lists or O(log n) trees — but require hashable keys and extra memory.

3. **Trees balance hierarchy:** O(log n) operations on a balanced tree beat O(n) linear structures for large datasets. Always check if your BST can become unbalanced.

4. **Graphs model real networks:** When your problem involves connections, relationships, or paths between entities, a graph is almost always the right model.

5. **Stack and Queue are specializations:** They restrict access intentionally — LIFO and FIFO discipline simplifies reasoning about algorithms that use them (DFS, BFS, undo systems).

6. **Amortized analysis matters:** A dynamic array's append is O(1) amortized, not O(1) always. Understand what "worst case" means for your use case.

7. **Space-time tradeoff is universal:** Hash maps trade memory for speed. Adjacency matrices trade memory for O(1) edge lookup. Sorted arrays trade write speed for O(log n) search.

---

## 12.2 Cheat Sheet

### Built-in Data Structures

| Structure | Ordered | Mutable | Allows Duplicates | Key Feature |
|---|---|---|---|---|
| List | Yes | Yes | Yes | Dynamic array, O(1) index |
| Tuple | Yes | No | Yes | Immutable, hashable |
| Set | No | Yes | No | O(1) membership test |
| Dict | Yes (3.7+) | Yes | Keys: No, Values: Yes | O(1) key-value lookup |
| array.array | Yes | Yes | Yes | Typed, contiguous numeric storage |

### User-Defined Data Structures

| Structure | Principle | Insert | Delete | Search | Best Use |
|---|---|---|---|---|---|
| Stack | LIFO | O(1) top | O(1) top | O(n) | DFS, undo, call stack |
| Queue | FIFO | O(1) rear | O(1) front | O(n) | BFS, scheduling |
| Linked List | Sequential chain | O(1) head | O(1) head | O(n) | Frequent head insert/delete |
| BST (balanced) | Sorted hierarchy | O(log n) | O(log n) | O(log n) | Sorted data, range queries |
| Heap | Partial order | O(log n) | O(log n) | O(1) min/max | Priority queues, Dijkstra |
| Graph | Network | O(1) | O(V) | O(V+E) | Network modeling, pathfinding |

### The Decision Tree

```
Need to store data:
│
├─ Fixed homogeneous numbers? → array.array or numpy.array
│
├─ Ordered, need index access? → List
│
├─ Immutable, use as dict key? → Tuple
│
├─ Fast membership test, no duplicates? → Set
│
├─ Key-value mapping? → Dict
│
├─ Need LIFO discipline? → Stack
│
├─ Need FIFO discipline? → Queue
│
├─ Frequent insert/delete at any position? → Linked List
│
├─ Need sorted data + fast search? → BST / AVL Tree
│
├─ Need min/max efficiently? → Heap
│
└─ Need to model relationships/network? → Graph
```

---

*Document compiled for self-study, interview preparation, and system design reference.*  
*Python 3.10+ used for all code examples.*  
*Last updated: April 2026*
