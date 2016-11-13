public class PhoneDirectory {

    LinkedHashSet<Integer> phoneNums;
    public PhoneDirectory(int maxNumbers) {
        int i=0;
        phoneNums = new LinkedHashSet<Integer>();
        for(;i<maxNumbers;i++)
            phoneNums.add(i);

    }

    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if(phoneNums.isEmpty())
            return -1;
        Iterator<Integer> iter = phoneNums.iterator();
        int nxt = iter.next();
        phoneNums.remove(nxt);
        return nxt;
    }

    /** Check if a number is available or not. */
    public boolean check(int number) {
        return phoneNums.contains(number);
    }

    /** Recycle or release a number. */
    public void release(int number) {
        phoneNums.add(number);
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */
