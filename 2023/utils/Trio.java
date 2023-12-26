package utils;

public class Trio <T, U, V> {
    private T first;
    private U second;
    private V third;

    public Trio(T first, U second, V third) {
        this.first = first;
        this.second = second;
        this.third = third;
    }

    public T getFirst() { return first; }

    public U getSecond() { return second; }

    public V getThird() { return third; }

    public void setFirst(T first) { this.first = first; }

    public void setSecond(U second) { this.second = second; }

    public void setThird(V third) { this.third = third; }

    @Override
    public String toString() {
        return "(" + first + ", " + second + ", " + third + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Trio) {
            Trio<?, ?, ?> other = (Trio<?, ?, ?>) obj;
            return first.equals(other.first) && second.equals(other.second) && third.equals(other.third);
        }
        return false;
    }

    @Override
    public int hashCode() {
        return first.hashCode() ^ second.hashCode() ^ third.hashCode();
    }
}
