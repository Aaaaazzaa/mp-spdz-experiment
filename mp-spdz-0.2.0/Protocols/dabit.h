/*
 * dabit.h
 *
 */

#ifndef PROTOCOLS_DABIT_H_
#define PROTOCOLS_DABIT_H_

#include <array>
using namespace std;

template<class T>
class dabit : public pair<T, typename T::bit_type::part_type>
{
    typedef pair<T, typename T::bit_type::part_type> super;

public:
    typedef typename T::bit_type::part_type bit_type;

    static int size()
    {
        return T::size() + bit_type::size();
    }

    static string type_string()
    {
        return T::type_string();
    }

    dabit()
    {
    }

    dabit(const T& a, const bit_type& b) :
            super(a, b)
    {
    }

    void assign(const char* buffer)
    {
        this->first.assign(buffer);
        this->second.assign(buffer + T::size());
    }
};

#endif /* PROTOCOLS_DABIT_H_ */
