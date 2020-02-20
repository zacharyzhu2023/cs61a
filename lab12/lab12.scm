(define (partial-sums stream)
  (define (helper sum-so-far stream)
    (if (null? stream) nil
      (cons-stream (+ sum-so-far (car stream)) (helper (+ sum-so-far (car stream)) (cdr-stream stream)))
    )
  )
  (helper 0 stream)
)
