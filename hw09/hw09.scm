
; Tail recursion

(define (replicate x n)
  (define (helper lst n)
       (if (= n 0) lst
           (helper (append (list x) lst) (- n 1))
        )
  )
  (helper nil n)
  )
(define (accumulate combiner start n term)
  (if (= n 1) (combiner (term n) start)
  (combiner (term n) (accumulate combiner start (- n 1) term)))
)

(define (accumulate-tail combiner start n term)
  (define (helper value-so-far counter)
    (if (= counter 0) value-so-far
        (helper (combiner value-so-far (term counter)) (- counter 1))
    )
  )
  (helper start n)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
      (cons-stream 3 (map-stream (lambda (x) (+ 3 x)) multiples-of-three)))


(define (nondecreastream s)
    (define (helper list-so-far s recent-elem)
        (cond
            ((null? s) (cons-stream list-so-far nil))
            ((null? list-so-far) (helper (list (car s)) (cdr-stream s) (car s)))
            ((>= (car s) recent-elem) (helper (append list-so-far (list (car s))) (cdr-stream s) (car s)))
            (else
                (cons-stream list-so-far (helper nil s 0))
            )
        )
    )
    (helper nil s 0)
    ; Thoughts: how can we avoid a comparison for the first element?
    ; Maybe can set recent-elem default to nil? And then check to see if it's nil?
    ; Are we allowed to nest if statements anyhow?
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))