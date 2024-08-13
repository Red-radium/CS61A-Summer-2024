(define (length s)
    (define (helper s n)
        (if (null? s) n
            (helper (cdr s) (+ 1 n))
    
        )
    )
    (helper s 0)
)

(define (runs s)
    (if (null? s) nil
        (let(p(next-run s)))
        (cons (first p)(runs(rest p)))
    )
)

(define (next-runs s)
    (if (or (null? (cdr s)) (< (cdr (car s)) (car s)))
        (pair (list (car s)) (cdr s))
        (begin
            (define p (next-runs (cdr s)))
            (pair (cons (car s) (first p)) (rest p))
        )
    )
)