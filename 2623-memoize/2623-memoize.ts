function memoize(fn) {
  const cache = {}; // Our 'memory' - a simple JavaScript object

  return function (...args) {
    // The inner function that does the magic
    const key = String(args); // Creates a unique key from the arguments

    if (key in cache) {
      // Have we seen this input before?
      return cache[key]; // Yes! Return the stored result
    }

    const result = fn(...args); // No? Call the original function
    cache[key] = result; // Store the result for next time
    return result; // Return the calculated result
  };
}