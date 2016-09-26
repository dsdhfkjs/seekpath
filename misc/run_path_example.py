if __name__ == '__main__':
    import os
    import ase, ase.io

    from kpaths3d import get_explicit_k_path
    import kpaths3d.hpkot as hpkot

    with_inv = True
    case = 'cP1'

    # Get the POSCAR with the example structure
    hpkot_folder = os.path.split(os.path.abspath(hpkot.__file__))[0]
    folder = os.path.join(hpkot_folder,"band_path_data",case)
    poscar_with_inv = os.path.join(folder,'POSCAR_inversion')
    poscar_no_inv = os.path.join(folder,'POSCAR_noinversion')

    poscar = poscar_with_inv if with_inv else poscar_no_inv
    asecell = ase.io.read(poscar)

    system = (asecell.get_cell(), asecell.get_scaled_positions(), 
        asecell.get_atomic_numbers())

    res = get_explicit_k_path(system, with_time_reversal=False) 

    for l, p in zip(res['explicit_kpoints_labels'], res['explicit_kpoints_abs']):
        print "{}\t{}".format(l, p)
    
    print res['explicit_kpoints_linearcoord']

    for l, p in zip(res['explicit_kpoints_labels'], res['explicit_kpoints_linearcoord']):
        print "{}\t{}".format(l, p)

    print len(res['explicit_kpoints_labels']), len(res['explicit_kpoints_abs']), \
        len(res['explicit_kpoints_linearcoord'])

    #for segment in res['segments']:
    #    print segment
    #    print res['explicit_kpoints_labels'][slice(*segment)]

