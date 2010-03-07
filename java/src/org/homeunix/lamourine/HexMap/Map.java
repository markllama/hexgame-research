/**
 *
 */
package org.homeunix.lamourine.HexMap;

import java.util.Collection;
import java.util.List;
import java.util.ListIterator;
import java.util.ArrayList;

/**
 * An array that has a non-zero base
 */
class BiasedArrayList <E> extends ArrayList <E> {
    protected int bias = 0;

    /**
     *
     */
    BiasedArrayList() {
	super();
	this.bias = 0;
    }

    /**
     *
     */
    BiasedArrayList(int bias) {
	super();
	this.bias = bias;
    }

    BiasedArrayList(int bias, Collection <E> c) {
	super(c);
	this.bias = bias;
    }

    BiasedArrayList(int bias, int initialCapacity) {
	super(initialCapacity);
	this.bias = bias;
    }

    /**
     *
     */
    public void setBias(int bias) {
	this.bias = bias;
    }

    /**
     *
     */
    public int getBias() {
	return this.bias;
    }

    /**
     *
     */
    public void add(int index, E e) {
	super.add(index - this.bias, e);
    }

    public E get(int index) {
	return super.get(index - this.bias);
    }
	     
    public int indexOf(Object o) {
	return super.indexOf(o) + this.bias;
    }

    public int lastIndexOf(Object o) {
	return super.lastIndexOf(o) + this.bias;
    }

    public ListIterator <E> listIterator(int index) {
	return super.listIterator(index - this.bias);
    }

    public E remove(int index) {
	return super.remove(index - this.bias);
    }

    protected void removeRange(int fromIndex, int toIndex) {
	super.removeRange(fromIndex - this.bias, toIndex - this.bias);
    }

    public E set(int index, E element) {
	return super.set(index - this.bias, element);
    }

    public List<E> subList(int fromIndex, int toIndex) {
	return super.subList(fromIndex - this.bias, toIndex - this.bias);
    }
}

public class Map {
    // an array of hexes
    Vector size = new Vector(15,22);
    Vector origin = new Vector(0,0);
    BiasedArrayList <BiasedArrayList <Hex>> hexes;
    ArrayList<Terrain> terrains;
    ArrayList<Token> tokens;

    Map() {
	this.size = new Vector(15,22);
	this.origin = Vector.ORIGIN;

	//this.fill();

	this.terrains = new ArrayList<Terrain>();
	this.tokens = new ArrayList<token>();
    }

    Map(Vector size) {
	this.size = size;
	this.origin = Vector.ORIGIN;

	//this.fill();

	this.terrains = new ArrayList<Terrain>();
	this.tokens = new ArrayList<token>();
    }

    Map(Vector size, Vector origin) {
	this.size = size;
	this.origin = origin;
	
	//this.fill();

	this.terrains = new ArrayList<Terrain>();
	this.tokens = new ArrayList<token>();
    }

    private void fill() {
	// create the hexes

	this.hexes = 
	    new BiasedArrayList<BiasedArrayList <Hex>>(this.origin.hx);

	for (int i = 0 ; i < this.size.hx ; i++) {
	    int hx = i + this.origin.hx;
	    int ybias = Map.ybias(hx);
	    BiasedArrayList<Hex> column = new BiasedArrayList<Hex>(ybias);
	    for (int j = 0 ; j < this.size.hy ; j++) {
		int hy = j + ybias;
		Hex hex = new Hex(new Vector(hx, hy), this);
		column.add(hex);
	    }
	    this.hexes.add(column);
	}
    }

    static int ybias(int hx) {
	return hx > 0 ? hx / 2 : (hx - 1) / 2;
    }

}
