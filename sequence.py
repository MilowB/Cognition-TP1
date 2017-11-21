from student import *

class Sequence:
    #Param : sequence - map de couple {actions, somme de récompenses}
    def __init__(self, sequence):
        self._sub_sequence = sequence
        self.student = None

    def _buildStudent(self):
        rewards = []
        for seq in self._sub_sequence:
            for i in range(len(seq)):
                rewards.append(i)                
        self.student = Student(rewards)

    def buildSequence(self):
        self._buildStudent()
        #print("self._sub_sequence : ", self._sub_sequence)
        mean = self._mean_sequence()
        #print("mean : ", mean)
        sequence = []
        agregation = []
        size = 0
        for i in range(len(self._sub_sequence)):
            reward = self._sub_sequence[i][len(self._sub_sequence[i]) - 1]
            if reward < mean and self.student.isSignificant(reward):
                pass
            else:
                sequence.append([])            
                for j in range(len(self._sub_sequence[i]) - 1):
                    sequence[size].append(0)
                    sequence[size][j] = self._sub_sequence[i][j]
                size += 1

        #print(sequence)
        for i in range(len(sequence) - 1):
            agregation.append([])
            for j in range(len(sequence[i])):
                agregation[i].append(sequence[i][j])
                agregation[i].append(sequence[i + 1][j])

        #print(agregation)
        return agregation
    
    def _mean_sequence(self):
        mean = 0.0
        for i in range(len(self._sub_sequence)):
            mean += self._sub_sequence[i][len(self._sub_sequence[i]) - 1]
        mean /= len(self._sub_sequence)
        return mean