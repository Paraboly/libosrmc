import sys

import pandas as pd

from osrmcpy import OSRM, Coordinate


# Example User Code
def main():
    if '--help' in sys.argv or '-h' in sys.argv:
        sys.exit('Usage: {} [OSRM data base path]'.format(sys.argv[0]))

    print(sys.argv[1])
    osrm = OSRM(sys.argv[1].encode('utf-8') if len(sys.argv) >= 2 else None, True)

    # Berlin
    # start = Coordinate(id=None, longitude=13.14117, latitude=52.41445)
    # end = Coordinate(id=None, longitude=13.55747, latitude=52.61437)
    # Ireland
    # start = Coordinate(id=None, longitude=-6.346509195699211, latitude=53.36407603954265)

    # params.coordinates.push_back({osrm::util::FloatLongitude{29.072002}, osrm::util::FloatLatitude{40.992023}});
    # params.coordinates.push_back({osrm::util::FloatLongitude{29.071907}, osrm::util::FloatLatitude{40.992329}});
    # params.coordinates.push_back({osrm::util::FloatLongitude{29.072044}, osrm::util::FloatLatitude{40.992508}});
    # params.coordinates.push_back({osrm::util::FloatLongitude{29.072222}, osrm::util::FloatLatitude{40.992565}});
    # params.coordinates.push_back({osrm::util::FloatLongitude{29.072504}, osrm::util::FloatLatitude{40.992546}});
    # params.coordinates.push_back({osrm::util::FloatLongitude{29.073633}, osrm::util::FloatLatitude{40.992191}});
    # params.coordinates.push_back({osrm::util::FloatLongitude{29.074406}, osrm::util::FloatLatitude{40.991718}});
    # end = Coordinate(id=None, longitude=-6.35272995922493, latitude=53.283447477339756)
    coordinates = [
        Coordinate(id=None, longitude=29.072002, latitude=40.992023),
        Coordinate(id=None, longitude=29.071907, latitude=40.992329),
        Coordinate(id=None, longitude=29.072044, latitude=40.992508),
        Coordinate(id=None, longitude=29.072222, latitude=40.992565),
        Coordinate(id=None, longitude=29.072504, latitude=40.992546),
        Coordinate(id=None, longitude=29.073633, latitude=40.992191),
        Coordinate(id=None, longitude=29.074406, latitude=40.991718)
    ]

    match = osrm.match(coordinates)

    if match:
        print("matched")
        # print(route)
        # print('Distance: {0:.0f} meters'.format(route.distance))
        # print('Duration: {0:.0f} seconds'.format(route.duration))
        # print('Geometry: {0}'.format(route.geometry))

        # df_geoms = pd.read_csv(csv_path, names=['id', 'distance', 'duration', 'polyline_geom'])
        # print(df_geoms.head(25))
        print(match.node_count)


    else:
        print('no matched')


if __name__ == '__main__':
    main()
