package BasicDataStructure;

import java.beans.BeanProperty;
import java.util.Arrays;

public class Stack {
    private int[] storage;
    private int capacity;
    private int count;
    private static final int FACTOR = 2;

    public Stack()
    {
        this.capacity = 8;
        this.storage = new int[8];
        this.count = 0;
    }

    public Stack(int initialCapacity)
    {
        if (initialCapacity < 0)
        {
            throw new IllegalArgumentException("Capacity too small");
        }

        this.capacity = initialCapacity;
        this.storage = new int[initialCapacity];
        this.count = 0;
    }

    public void push(int value)
    {
        if (this.count == this.capacity)
        {
            ensureCapacity();
        }
        this.storage[this.count] = value;
        this.count++;
    }

    public int pop()
    {
        if (this.count == 0)
        {
            throw new IllegalArgumentException("Empty stack");
        }

        this.count--;
        return this.storage[this.count];
    }

    public int peek()
    {
        if (this.count == 0)
        {
            throw new IllegalArgumentException("Empty stack");
        }

        return this.storage[this.count-1];
    }

    public boolean isEmpty()
    {
        return this.count == 0;
    }

    public int size()
    {
        return this.count;
    }

    private void ensureCapacity()
    {
        this.capacity *= FACTOR;
        this.storage = Arrays.copyOf(this.storage, this.capacity);
    }
}
