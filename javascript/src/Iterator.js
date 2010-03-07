/**
 * @fileoverview
 * An iterator interface
 *
 * @author Mark Lamourine <markllama@gmail.com>
 * @version 1.0
 */

/**
 * @class
 * That object is expected to provide two methods:
 * <br>&lt;Object&gt; first() returns the first object in the series
 * <br>&lt;Object&gt; next(&lt;Object&gt; current) returns the next object in the series or null 
 * after the last element.
 * @constructor
 * Create an Iterator for the object provided.
 * @param {Object} obj the object to be iterated
 * @return {Iterator &lt;Object&gt;}
 */
function Iterator(obj) {
    /**
     * An that object that becomes iterable.
     * @private
     * @type Object
     */
    this.object = obj;

    /**
     * The current value of the iterator.
     * @private
     * @type Object
     */
    this.curr = null;
    this.reset();
};

/**
 * Reset the iterator to the beginning of the series.
 * @return {void}
 */
Iterator.prototype.reset = function() {    
    this.curr = this.object.first();
};

/**
 * Return the current object in the series.
 * @return {&lt;Object&gt;} The current object.
 */
Iterator.prototype.current = function() {
    return this.curr;
};

/**
 * Return the next object in the series.
 * @param {Boolean} increment: update the current object. (default: true)
 * @return {&lt;Object&gt;} The next object in the series.
 */
Iterator.prototype.next = function(increment) {
    var current = this.curr;
    if (increment == true || increment == null) {
	this.curr = this.object.next(current);
    }
    return current;
};

Iterator.prototype.toString = function() {
    return '[object Iterator]';
};