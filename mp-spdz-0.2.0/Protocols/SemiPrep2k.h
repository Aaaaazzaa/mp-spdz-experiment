/*
 * SemiPrep2k.h
 *
 */

#ifndef PROTOCOLS_SEMIPREP2K_H_
#define PROTOCOLS_SEMIPREP2K_H_

#include "SemiPrep.h"
#include "RepRingOnlyEdabitPrep.h"

template<class T>
class SemiPrep2k : public SemiPrep<T>, public RepRingOnlyEdabitPrep<T>
{
    void buffer_edabits(int n_bits, ThreadQueues* queues)
    {
        RepRingOnlyEdabitPrep<T>::buffer_edabits(n_bits, queues);
    }

    void buffer_edabits(bool strict, int n_bits, ThreadQueues* queues)
    {
        BufferPrep<T>::buffer_edabits(strict, n_bits, queues);
    }

    void buffer_sedabits(int n_bits, ThreadQueues*)
    {
        this->buffer_sedabits_from_edabits(n_bits);
    }

public:
    SemiPrep2k(SubProcessor<T>* proc, DataPositions& usage) :
            BufferPrep<T>(usage), BitPrep<T>(proc, usage),
            OTPrep<T>(proc, usage),
            RingPrep<T>(proc, usage),
            SemiHonestRingPrep<T>(proc, usage),
            SemiPrep<T>(proc, usage),
            RepRingOnlyEdabitPrep<T>(proc, usage)
    {
    }

    void get_dabit_no_count(T& a, typename T::bit_type& b)
    {
        this->get_one_no_count(DATA_BIT, a);
        b = a & 1;
    }
};

#endif /* PROTOCOLS_SEMIPREP2K_H_ */
