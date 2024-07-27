(define (square n) (* n n))

(define (pow base exp)
    (cond
    ((= exp 1) base)
    ((odd? exp) (* base (pow base (- exp 1))))
    (else (pow (square base) (quotient exp 2)))
    )
)

(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let ((y (repeatedly-cube (- n 1) x)))
            (* y y y)
        )
    )
)

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? s)
    (if (null? s) #t
        (if (null? (cdr s)) #t
            (if (< (cadr s) (car s)) #f
                (ascending? (cdr s))
            )
        )
    )
)

(define (my-filter pred s)
    (if (null? s) nil
        (if (pred (car s)) (cons (car s) (my-filter pred (cdr s)))
            (my-filter pred (cdr s))
        )
    )
)

(define (no-repeats s)
    (cond
        ((null? s) nil)
        (else 
            (cons (car s) (no-repeats (my-filter (lambda (x) (not (= x (car s)))) (cdr s)))
            )
        )
    )
)


; helper function
; returns the values of lst that are bigger than x
; e.g., (larger-values 3 '(1 2 3 4 5 1 2 3 4 5)) --> (4 5 4 5)
(define (larger-values x lst)
    (if (null? lst) nil
        (if (>(car lst) x) (cons (car lst) (larger-values x (cdr lst)))
            (larger-values x (cdr lst))
        )
    )
)

(define (longest-increasing-subsequence lst)
    (if (null? lst)
        nil
        (begin (define first (car lst))
            (define rest (cdr lst))
            (define large-values-rest
                (larger-values first rest))
            (define with-first
                (cons first (longest-increasing-subsequence large-values-rest))
            )
            (define without-first
                (longest-increasing-subsequence rest)
            )
            (if (> (length with-first) (length without-first))
                with-first
                without-first
            )
        )
    )
)