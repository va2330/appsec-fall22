from bcc import BPF
[IMPORT OTHER MODULES IF NEEDED]

BPF_PROGRAM = r"""
[ADD YOUR CODE, IF ANY]
"""

bpf = BPF(text=BPF_PROGRAM)
[ADD YOUR CODE, IF ANY]

while True:
    [MODIFY THIS LOOP TO RUN FOR ONLY 7 SECONDS]
    try:
        [ADD YOUR CODE, IF ANY] = bpf.trace_fields()
        [ADD YOUR CODE, IF ANY]

    except ValueError:
        continue
