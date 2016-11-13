// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {

    Integer cache;
    Iterator<Integer> list;

    public PeekingIterator(Iterator<Integer> iterator) {
        // initialize any member here.
        list = iterator;
        cache = null;
    }

    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() {
        if(cache==null && list.hasNext())
            cache = list.next();
        return cache;
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() {
        Integer tmp = peek();
        cache = null;
        return tmp;
    }

    @Override
    public boolean hasNext() {
        return peek()!=null;
    }
}
