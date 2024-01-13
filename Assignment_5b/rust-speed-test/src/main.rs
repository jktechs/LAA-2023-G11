use na::{DMatrix, DVector};
use nalgebra_lapack::LU;
use nalgebra_lapack::SVD;
use std::time::Instant;
fn main() {    
    const SIZE_A: usize = 3000;
    const SIZE_SMALL_A: usize = 1100;
    const SIZE_SMALL_B: usize = 6000;

    let a = DMatrix::from_iterator(SIZE_A, SIZE_A, (0..(SIZE_A * SIZE_A)).map(|_| rand::random::<f64>()));
    let b = DVector::from_iterator(SIZE_A, (0..SIZE_A).map(|_| rand::random::<f64>()));

    let small_a = DMatrix::from_iterator(SIZE_SMALL_A, SIZE_SMALL_A, (0..(SIZE_SMALL_A * SIZE_SMALL_A)).map(|_| rand::random::<f64>()));
    let small_b = DVector::from_iterator(SIZE_SMALL_B, (0..SIZE_SMALL_B).map(|_| rand::random::<f64>()));

    println!("Calculating A * x = b ({} x {})", SIZE_A, SIZE_A);
    let now = Instant::now();
    let tmp = LU::new(a).solve(&b).unwrap();
    println!("Done {:?}", now.elapsed());
    core::hint::black_box(tmp);

    println!("Calculating SVD of A ({} x {})", SIZE_SMALL_A, SIZE_SMALL_A);
    let now = Instant::now();
    let tmp = SVD::new(small_a).unwrap();
    println!("Done {:?}", now.elapsed());
    core::hint::black_box(tmp);

    println!("Calculating 10^6 inner products ({})", SIZE_SMALL_B);
    let now = Instant::now();
    for _ in 0..1_000_000 {
        core::hint::black_box(small_b.transpose() * &small_b);
    }
    println!("Done {:?}", now.elapsed());
}