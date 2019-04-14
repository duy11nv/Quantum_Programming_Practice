# random bit generator circuit in Qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
from qiskit import BasicAer
qreg = QuantumRegister(1)
creg = ClassicalRegister(1)
qcircuit = QuantumCircuit(qreg, creg)
qcircuit.h(qreg[0])
qcircuit.measure(qreg[0],creg[0])


backend = BasicAer.get_backend('qasm_simulator')
result=execute(qcircuit, backend=backend, shots=1).result()
        
print(result.get_counts())
    
