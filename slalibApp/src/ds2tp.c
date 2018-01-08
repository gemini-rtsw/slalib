#include "slalib.h"
#include "slamac.h"
#include "epicsStdioRedirect.h"
void slaDs2tp ( double ra, double dec, double raz, double decz,
                double *xi, double *eta, int *j )
/*
**  - - - - - - - - -
**   s l a D s 2 t p
**  - - - - - - - - -
**
**  Projection of spherical coordinates onto tangent plane
**  ('gnomonic' projection - 'standard coordinates').
**
**  (double precision)
**
**  Given:
**     ra,dec      double   spherical coordinates of point to be projected
**     raz,decz    double   spherical coordinates of tangent point
**
**  Returned:
**     *xi,*eta    double   rectangular coordinates on tangent plane
**     *j          int      status:   0 = OK, star on tangent plane
**                                    1 = error, star too far from axis
**                                    2 = error, antistar on tangent plane
**                                    3 = error, antistar too far from axis
**
**  Last revision:   18 July 1996
**
**  Copyright P.T.Wallace.  All rights reserved.
*/
#define TINY 1e-6
{
   double sdecz, sdec, cdecz, cdec, radif, sradif, cradif, denom;

   if ( !ra || !dec || !raz || !decz ) {
       printf("slaDs2tp: Invalid input values: ra=%f dec=%f raz=%f decz=%f \n",ra, dec, raz, decz);
       *xi  = TINY;
       *eta = TINY;
       *j   = 0;
       return;
   }

/* Trig functions */
   sdecz = sin ( decz );
   sdec = sin ( dec );
   cdecz = cos ( decz );
   cdec = cos ( dec );
   radif = ra - raz;
   sradif = sin ( radif );
   cradif = cos ( radif );

/* Reciprocal of star vector length to tangent plane */
   denom = sdec * sdecz + cdec * cdecz * cradif;

/* Handle vectors too far from axis */
   if ( denom > TINY ) {
      *j = 0;
   } else if ( denom >= 0.0 ) {
      *j = 1;
      printf("slaDs2tp: j=1 denom=%f sdec=%f sdecz=%f cdec=%f cdecz=%f cradif=%f TINY=%f \n",
      			denom,sdec,sdecz,cdec,cdecz,cradif,TINY);
      denom = TINY;
   } else if ( denom > -TINY ) {
      *j = 2;
      printf("slaDs2tp: j=2 denom=%f sdec=%f sdecz=%f cdec=%f cdecz=%f cradif=%f TINY=%f \n",
      			denom,sdec,sdecz,cdec,cdecz,cradif,TINY);
      denom = -TINY;
   } else {
      printf("slaDs2tp: j=3 denom=%f sdec=%f sdecz=%f cdec=%f cdecz=%f cradif=%f TINY=%f ra=%f dec=%f\n",
      			denom,sdec,sdecz,cdec,cdecz,cradif,TINY,ra,dec);
      *j = 3;
   }

/* Compute tangent plane coordinates (even in dubious cases) */
   if ( denom ) {
   *xi = cdec * sradif / denom;
   *eta = ( sdec * cdecz - cdec * sdecz * cradif ) / denom;
   }
}
