use na::{DMatrix, DVector};
use std::time::Instant;
fn main() {    
    const SIZE_A: usize = 3000;
    const SIZE_SMALL_A: usize = 1300;
    const SIZE_SMALL_B: usize = 220;

    let a = DMatrix::from_iterator(SIZE_A, SIZE_A, (0..(SIZE_A * SIZE_A)).map(|_| rand::random::<f64>()));
    let b = DVector::from_iterator(SIZE_A, (0..SIZE_A).map(|_| rand::random::<f64>()));

    let small_a = DMatrix::from_iterator(SIZE_SMALL_A, SIZE_SMALL_A, (0..(SIZE_SMALL_A * SIZE_SMALL_A)).map(|_| rand::random::<f64>()));
    let small_b = DVector::from_iterator(SIZE_SMALL_B, (0..SIZE_SMALL_B).map(|_| rand::random::<f64>()));

    println!("Calculating A * x = b ({} x {})", SIZE_A, SIZE_A);
    let now = Instant::now();
    core::hint::black_box(a.clone().lu().solve(&b).unwrap());
    println!("Done {:?}", now.elapsed());

    println!("Calculating SVD of A ({} x {})", SIZE_SMALL_A, SIZE_SMALL_A);
    let now = Instant::now();
    core::hint::black_box(small_a.svd_unordered(true, true));
    println!("Done {:?}", now.elapsed());

    println!("Calculating 10^6 inner products ({})", SIZE_SMALL_B);
    let now = Instant::now();
    for _ in 0..1_000_000 {
        core::hint::black_box(&small_b * small_b.transpose());
    }
    println!("Done {:?}", now.elapsed());
}