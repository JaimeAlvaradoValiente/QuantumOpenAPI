import connexion
import six

from openapi_server import util



from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi


def grover_circuit():  # noqa: E501
    
    """Get the circuit implementation of Grover Algorithm

     # noqa: E501


    :rtype: None
    """


        
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)
    
    circuit.reset(qreg_q[0])
    circuit.reset(qreg_q[1])
    circuit.h(qreg_q[1])
    circuit.h(qreg_q[0])
    circuit.x(qreg_q[1])
    circuit.x(qreg_q[0])
    circuit.cz(qreg_q[0], qreg_q[1])
    circuit.x(qreg_q[0])
    circuit.x(qreg_q[1])
    circuit.h(qreg_q[0])
    circuit.h(qreg_q[1])
    circuit.z(qreg_q[0])
    circuit.z(qreg_q[1])
    circuit.cz(qreg_q[0], qreg_q[1])
    circuit.h(qreg_q[0])
    circuit.h(qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])

    return 'do some magic!'



from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ


def random_circuit(api_token):  # noqa: E501
    
    """Get the circuit implementation for random numbers

     # noqa: E501

    :param api_token: API Token
    :type api_token: str

    :rtype: None
    """


        
    IBMQ.enable_account(api_token)
    provider = IBMQ.get_provider(hub='ibm-q')
    
    q = QuantumRegister(16,'q')
    c = ClassicalRegister(16,'c')
    circuit = QuantumCircuit(q,c)
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits 
    
    backend = provider.get_backend('ibmq_qasm_simulator')
    job = execute(circuit, backend, shots=1)
                                   
    print('Executing Job...\n')                 
    result = job.result()
    counts = result.get_counts(circuit)
    
    print('RESULT: ',counts,'\n')
    print('Press any key to close')
    input()

    return 'do some magic!'
