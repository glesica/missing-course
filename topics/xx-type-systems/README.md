# Type Systems

It is a common refrain from students that types "get in the way" when
programming. While we have all experienced frustration trying to convince a
compiler to run a program we believed to be valid, types, as concepts, are much
more fundamental than this.

The goal of this lecture is to suggest a way of thinking about types that will,
hopefully, be useful with any programming language, even those with little
syntactic emphasis on types, and reduce the frustration associated with this
concepts in languages that do feature types as syntactic elements.

## The World is Full of Types

We deal with types seamlessly in our daily lives. When we go to a restuarant, we
don't expect the people at the next table to take our order or refill our
drinks, we expect the wait staff to do that. Said another (super weird) way, we
don't call the `refill_drinks()` method on the folks at the next table, because
we know, implicitly, that they don't respond to that method.

Have you ever skipped lunch and then tried to take a bite out of your laptop?
Probably not, but, if you did, it probably didn't work out very well for you.
Laptops have `is_edible` set to `false` (or, if you prefer, they don't don't
implement the `Food` interface). They have the wrong type.

The point here is that the actual world around us has types. We would call it
"strongly typed" because every object in the world does, in fact, have a set of
specific types. Some of those types are complicated (imagine a chair made out of
chocolate), and they can change depending on context (a waiter eating at a
restaurant), but they exist nonetheless.

## Types in Programs

Just as the entire world is full of types, every programming language has types,
whether they are made explicit or not. For example, the code below only makes
sense if `x` has a `round(n)` method, otherwise its result will be an error of
some kind (depending on the language):

```javascript
function prettify(x) {
    return x.round(2);
}
```

So, despite the fact that no types were specified, they still exist. There isn't
necessarily a name that we could use to describe the type of `x` concisely, its
type is defined by the methods called on it. In this case, any object that has a
`round(n)` method satisfies the type. But even though its type is, perhaps,
ill-defined, it does, in fact, exist.

### Duck Typing

When we perform this sort of analysis in a programming language without explicit
types we apply "Duck Typing" (if it quacks like a duck, it's probably a duck).
In this case, we might replace "quacking" with "rounding".

As an aside, can you think of anything that quacks like a duck but isn't
actually a duck? What about the code above, can you think of a type that might
have a `round(n)` method that wouldn't necessarily make sense as an argument to
this function?

Languages that rely on Duck Typing are "dynamically typed" because the types are
handled at runtime (just like "dynamic analysis" is performed by running the
program). There is another category of languages, including popular examples
like Java, that are "statically typed" because types are specified (in one way
or another) in the actual program code and can be "checked" (or "enforced")
without running the program.

### Nominal Typing

One nice feature of Duck Typing is that it doesn't require us to do anything to
guarantee that a value will "work" in a particular situation, we just have to
make sure it has the required fields or methods. For instance, in Javascript,
`x` could be an entirely anonymous object, created on the fly, there is no need
for it to be declared in a particular way.

```javascript
prettify({
    round: function() {
        // Code goes here
    },
});
```

On the other hand, in order to determine the type that we're supposed to provide
for `x`, we need to study the entire body of the function to see how the value
is actually used. Further, if the function changes, we may need to update how we
use it. For example, assume someone changed `prettify(x)` to call a different
method on `x`.


```javascript
function prettify(x) {
    return x.floor();
}
```

Now, instead of passing in something that has a `round(n)` method, we need to
give it something that has a `floor()` method. But we have no way of knowing
this unless we study the updated code.

To get around this shortcoming, we can label `x` to make it easier to identify
such changes. In fact, once we do this, it is straightforward to determine
whether our types are correct statically, that is, without running the program.

For example, we could update the function to declare that `x` must be a `number`
(which seems reasonable). Now, only instances of the `number` type will be
allowed, and the program will refuse to compile (or run) at all if we fail to
adhere to this requirement.

```typescript
function prettify(x: number) {
    return x.round(2);
}
```

Further, if someone decides to use `floor()` instead of `round(n)`, we won't
need to update our code at all (assuming those are both methods on `number`).

One drawback, though, is that we have forced callers to provide an instance of
`number` even though we only actually intend to use a small piece of the
functionality that `number` provides. Additionally, the function can no longer
accept arbitrary, but compatible, types, like the anonymous object we
constructed above.

### Structural Typing

To get around these problems, we might declare an interface and then allow `x`
to have any type that implements the interface. However, at least in languages
like Java, that still requires the type of `x` to declare that it implements the
interface. In other words, we still can't provide an anonymous object the way we
could with Duck Typing.

```java
interface Roundable { ... }

class MyRoundable implements Roundable { ... }
```

Some languages, therefore, relax this latter requirement and provide what is
known as "Structural Typing". In this case, we must name (or otherwise specify,
see below) the type of `x`, but we can pass any value for `x` as long as it
satisfies the required interface, regardless of whether it has been declared to
satisfy the interface.

```typescript
function prettify(x: Roundable) {
    return x.round(2);
}
```

In some languages, we don't even have to name these interfaces, we can declare
them anonymously, inline. For example, we could write the `prettify(x)` function
to declare that it uses the `round(n)` method right in the function header.

```typescript
function prettify(x: { round: (n: number) => number }) {
    return x.round(2);
}
```

Note, however, that calling any method on `x` other than `round(n)` within the
body of `prettify(x)` will now result in a (static) type error because that is
the only method we have declared. Once we need more than one method or field in
our type declaration, it is usually best to use a named interface instead.

## Big Picture

At the end of the day, a programming language is a tool, and each contains,
embedded within its design, a set of trade-offs that give it advantages and
disadvantages, depending on the task to be completed.

Type systems are among the dimensions along which these trade-offs are made.
Some languages allow enormous amounts of information to be embedded in types,
others omit types entirely from their syntax.

Programmers must remember that types are pervasive in the world, and exist
in all programming languages, regardless of syntax. At the same time, they
should make the best possible use of the language at hand.

