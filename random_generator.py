# random bit generator circuit in Qiskit
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute

qreg = QuantumRegister(1)
creg = ClassicalRegister(1)
qcircuit = QuantumCircuit(qreg, creg)
qcircuit.h(qreg[0])
qcircuit.measure(qreg[0],creg[0])

result=execute(qcircuit, backend='local_qasm_simulator', shots=1).result()
        
print(result.get_counts())
    
